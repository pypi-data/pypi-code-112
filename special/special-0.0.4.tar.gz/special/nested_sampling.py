#! /usr/bin/env python

"""
Module with functions for posterior sampling of the model spectra parameters 
using nested sampling (``nestle``).
"""



__author__ = 'V. Christiaens, C. A. Gomez Gonzalez',
__all__ = ['nested_spec_sampling',
           'nested_sampling_results']

from astropy import constants as con
import nestle
import numpy as np
from matplotlib import pyplot as plt
from .config import time_ini, timing
from .fits import open_fits, write_fits
from .mcmc_sampling import lnlike, confidence, show_walk_plot, show_corner_plot
from .model_resampling import make_resampled_models
from os.path import isfile
from scipy.special import ndtri


def nested_spec_sampling(init, lbda_obs, spec_obs, err_obs, dist, 
                         grid_param_list, labels, bounds, resamp_before=True, 
                         model_grid=None, model_reader=None, em_lines={}, 
                         em_grid={}, dlbda_obs=None, instru_corr=None, 
                         instru_fwhm=None, instru_idx=None, filter_reader=None, 
                         AV_bef_bb=False, units_obs='si', units_mod='si', 
                         interp_order=1, priors=None, physical=True, 
                         interp_nonexist=True, output_dir='special/', 
                         grid_name='resamp_grid.fits', method='single', 
                         npoints=100, dlogz=0.1, decline_factor=None, 
                         rstate=None, verbose=True, **kwargs):
                            
    
    """ Runs a nested sampling algorithm in order to determine the position and
    the flux of the planet using the 'Negative Fake Companion' technique. The
    result of this procedure is a a ``nestle`` object containing the samples
    from the posterior distributions of each of the 3 parameters. It provides
    pretty good results (value plus error bars) compared to a more CPU intensive
    Monte Carlo approach with the affine invariant sampler (``emcee``).

    Parameters
    ----------
    init: numpy ndarray or tuple
        Initial guess on the best fit parameters of the spectral fit. Length of 
        the tuple should match the total number of free parameters. 
        - first all parameters related to loaded models (e.g. 'Teff', 'logg')
        - then the planet photometric radius 'R', in Jupiter radius
        - (optionally) the intensity of emission lines (labels must match \
        those in the em_lines dict), in units of the model spectrum (x mu)
        - (optionally) the optical extinction 'Av', in mag
        - (optionally) the ratio of total to selective optical extinction 'Rv'
        - (optionally) 'Tbb1', 'Rbb1', 'Tbb2', 'Rbb2', etc. for each extra bb \
        contribution
    lbda_obs : numpy 1d ndarray or list
        Wavelength of observed spectrum. If several instruments, should be 
        ordered per instrument, not necessarily as monotonically increasing 
        wavelength. Hereafter, n_ch = len(lbda_obs).
    spec_obs : numpy 1d ndarray or list
        Observed spectrum for each value of lbda_obs.
    err_obs : numpy 1d/2d ndarray or list
        Uncertainties on the observed spectrum. If 2d array, should be [2,n_ch]
        where the first (resp. second) column corresponds to lower (upper) 
        uncertainty, and n_ch is the length of lbda_obs and spec_obs.
    dist :  float
        Distance in parsec, used for flux scaling of the models.
    grid_param_list : list of 1d numpy arrays/lists OR None
        - If list, should contain list/numpy 1d arrays with available grid of \
        model parameters. 
        - Set to None for a pure n-blackbody fit, n=1,2,...
        - Note1: model grids should not contain grids on radius and Av, but \
        these should still be passed in initial_state (Av optional).
        - Note2: for a combined grid model + black body, just provide \
        the grid parameter list here, and provide values for 'Tbbn' and 'Rbbn' \
        in initial_state, labels and bounds.
    labels: Tuple of strings
        Tuple of labels in the same order as initial_state, that is:
        - first all parameters related to loaded models (e.g. 'Teff', 'logg')
        - then the planet photometric radius 'R', in Jupiter radius
        - (optionally) the flux of emission lines (labels should match those \
        in the em_lines dictionary), in units of the model spectrum (times mu)
        - (optionally) the optical extinction 'Av', in mag
        - (optionally) the ratio of total to selective optical extinction 'Rv'
        - (optionally) 'Tbb1', 'Rbb1', 'Tbb2', 'Rbb2', etc. for each extra bb \
        contribution.      
    bounds: dictionary
        Each entry should be associated with a tuple corresponding to lower and 
        upper bounds respectively. Bounds should be provided for ALL model
        parameters, including 'R' (planet photometric radius). 'Av' (optical 
        extinction) is optional. If provided here, Av will also be fitted.
        Example for BT-SETTL: bounds = {'Teff':(1000,2000), 'logg':(3.0,4.5),
        'R':(0.1,5), 'Av':(0.,2.5)}
        'M' can be used for a prior on the mass of the planet. In that case the
        corresponding prior log probability is computed from the values for 
        parameters 'logg' and 'R' (if both exist).
    resamp_before: bool, optional
        Whether to prepare the whole grid of resampled models before entering 
        the MCMC, i.e. to avoid doing it at every MCMC step. Recommended.
        Only reason not to: model grid is too large and individual models 
        require being opened and resampled at each step.
    model_grid : numpy N-d array, optional
        If provided, should contain the grid of model spectra for each
        free parameter of the given grid. I.e. for a grid of n_T values of Teff 
        and n_g values of Logg, the numpy array should be n_T x n_g x n_ch x 2, 
        where n_ch is the number of wavelengths for the observed spectrum,
        and the last 2 dims are for wavelength and fluxes respectively.
        If provided, takes precedence over filename/file_reader.
    model_reader : python routine, optional
        External routine that reads a model file and returns a 2D numpy array, 
        where the first column corresponds to wavelengths, and the second 
        contains model values. See example routine in model_interpolation() 
        description.
    em_lines: dictionary, opt
        Dictionary of emission lines to be added on top of the model spectrum.
        Each dict entry should be the name of the line, assigned to a tuple of
        4 values: 
        1) the wavelength (in mu); 
        2) a string indicating whether line intensity is expressed in flux 
        ('F'), luminosity ('L') or log(L/LSun) ("LogL");
        3) the FWHM of the gaussian (or None if to be set automatically); 
        4) whether the FWHM is expressed in 'nm', 'mu' or 'km/s'. 
        The third and fourth can also be set to None. In that case, the FWHM of 
        the gaussian will automatically be set to the equivalent width of the
        line, calculated from the flux to be injected and the continuum 
        level (measured in the grid model to which the line is injected). 
        Examples: 
        em_lines = {'BrG':(2.1667,'F', None, None)};
        em_lines = {'BrG':(2.1667,'LogL', 100, 'km/s')}
    em_grid: dictionary pointing to lists, opt
        Dictionary where each entry corresponds to an emission line and points
        to a list of values to inject for emission line fluxes. For computation 
        efficiency, interpolation will be performed between the points of this 
        grid during the MCMC sampling. Dict entries should match labels and 
        em_lines.
    dlbda_obs: numpy 1d ndarray or list, optional
        Spectral channel width for the observed spectrum. It should be provided 
        IF one wants to weigh each point based on the spectral 
        resolution of the respective instruments (as in Olofsson et al. 2016).
    instru_corr : numpy 2d ndarray or list, optional
        Spectral correlation throughout post-processed images in which the 
        spectrum is measured. It is specific to the combination of instrument, 
        algorithm and radial separation of the companion from the central star.
        Can be computed using distances.spectral_correlation(). In case of
        a spectrum obtained with different instruments, build it with
        distances.combine_corrs(). If not provided, it will consider the 
        uncertainties in each spectral channels are independent. See Greco & 
        Brandt (2017) for details.
    instru_fwhm : float OR list of either floats or strings, optional
        The instrumental spectral fwhm provided in nm. This is used to convolve
        the model spectrum. If several instruments are used, provide a list of 
        instru_fwhm values, one for each instrument whose spectral resolution
        is coarser than the model - including broad band filter FWHM if 
        relevant.
        If strings are provided, they should correspond to filenames (including 
        full paths) of text files containing the filter information for each 
        observed wavelength. Strict format: 
    instru_idx: numpy 1d array, optional
        1d array containing an index representing each instrument used 
        to obtain the spectrum, label them from 0 to n_instru. Zero for points 
        that don't correspond to any instru_fwhm provided above, and i in 
        [1,n_instru] for points associated to instru_fwhm[i-1]. This parameter 
        must be provided if the spectrum consists of points obtained with 
        different instruments.
    filter_reader: python routine, optional
        External routine that reads a filter file and returns a 2D numpy array, 
        where the first column corresponds to wavelengths, and the second 
        contains transmission values. Important: if not provided, but strings 
        are detected in instru_fwhm, the default file reader will be used. 
        It assumes the following format for the files:
        - first row containing header
        - starting from 2nd row: 1st column: wavelength, 2nd col.: transmission
        - Unit of wavelength can be provided in parentheses of first header \
        key name: e.g. "WL(AA)" for angstrom, "wavelength(mu)" for micrometer \
        or "lambda(nm)" for nanometer. Note: Only what is in parentheses \
        matters.
        Important: filter files should all have the same format and WL units.
    AV_bef_bb: bool, optional
        If both extinction and an extra bb component are free parameters, 
        whether to apply extinction before adding the BB component (e.g. 
        extinction mostly from circumplanetary dust) or after the BB component
        (e.g. mostly insterstellar extinction).
    units_obs : str, opt {'si','cgs','jy'}
        Units of observed spectrum. 'si' for W/m^2/mu; 'cgs' for ergs/s/cm^2/mu 
        or 'jy' for janskys.
    units_mod: str, opt {'si','cgs','jy'}
        Units of the model. 'si' for W/m^2/mu; 'cgs' for ergs/s/cm^2/mu or 'jy'
        for janskys. If different to units_obs, the spectrum units will be 
        converted.
    interp_order: int, opt, {-1,0,1} 
        Interpolation mode for model interpolation.
        -1: log interpolation (i.e. linear interpolatlion on log(Flux))
        0: nearest neighbour model.
        1: Order 1 spline interpolation.
    priors: dictionary, opt
        If not None, sets prior estimates for each parameter of the model. Each 
        entry should be set to either None (no prior) or a tuple of 2 elements 
        containing prior estimate and uncertainty on the estimate.
        Missing entries (i.e. provided in bounds dictionary but not here) will
        be associated no prior.
        e.g. priors = {'Teff':(1600,100), 'logg':(3.5,0.5), 'R':(1.6,0.1), 
        'Av':(1.8,0.2), 'M':(10,3)}
        Important: dictionary entry names should match exactly those of bounds.
    physical: bool, opt
        In case of extra black body component(s) to a photosphere, whether to 
        force lower temperature than the photosphere effective temperature.
    interp_nonexist: bool, opt
        Whether to interpolate non-existing models in the grid. Only used if 
        resamp_before is set to True.
    w : float or tuple
        The relative size of the bounds (around the initial state ``init``) for 
        each parameter. If a float the same relative size is considered for 
        each parameter. E.g. if 0.1, bounds will be set to:
        (0.9*params[0], 1.1*params[0]),
        ...
        (0.9*params[N-1], 1.1*params[N-1]),
        to True), or make it and write it if it does not.
    output_dir: str, optional
        The name of the output directory which contains the output files in the 
        case  ``save`` is True.   
    grid_name: str, optional
        Name of the fits file containing the model grid (numpy array) AFTER
        convolution+resampling as the observed spectrum given as input.
        If provided, will read it if it exists (and resamp_before is set
    method : {"single", "multi", "classic"}, str optional
        Flavor of nested sampling.
    npoints : int optional
        Number of active points. At least ndim+1 (4 will produce bad results).
        For problems with just a few parameters (<=5) like the NEGFC, good
        results are obtained with 100 points (default).
    dlogz : Estimated remaining evidence
        Iterations will stop when the estimated contribution of the remaining
        prior volume to the total evidence falls below this threshold.
        Explicitly, the stopping criterion is log(z + z_est) - log(z) < dlogz
        where z is the current evidence from all saved samples, and z_est is the
        estimated contribution from the remaining volume. This option and
        decline_factor are mutually exclusive. If neither is specified, the
        default is dlogz=0.5.
    decline_factor : float, optional
        If supplied, iteration will stop when the weight (likelihood times prior
        volume) of newly saved samples has been declining for
        decline_factor * nsamples consecutive samples. A value of 1.0 seems to
        work pretty well.
    rstate : random instance, optional
        RandomState instance. If not given, the global random state of the
        numpy.random module will be used.
    kwargs: optional
        Additional optional arguments to the `nestle.sample` function.

    Returns
    -------
    res : nestle object
        ``Nestle`` object with the nested sampling results, including the
        posterior samples.

    Notes
    -----
    Nested Sampling is a computational approach for integrating posterior
    probability in order to compare models in Bayesian statistics. It is similar
    to Markov Chain Monte Carlo (MCMC) in that it generates samples that can be
    used to estimate the posterior probability distribution. Unlike MCMC, the
    nature of the sampling also allows one to calculate the integral of the
    distribution. It also happens to be a pretty good method for robustly
    finding global maxima.

    Nestle documentation:
    http://kbarbary.github.io/nestle/

    Convergence:
    http://kbarbary.github.io/nestle/stopping.html
    Nested sampling has no well-defined stopping point. As iterations continue,
    the active points sample a smaller and smaller region of prior space.
    This can continue indefinitely. Unlike typical MCMC methods, we don't gain
    any additional precision on the results by letting the algorithm run longer;
    the precision is determined at the outset by the number of active points.
    So, we want to stop iterations as soon as we think the active points are
    doing a pretty good job sampling the remaining prior volume - once we've
    converged to the highest-likelihood regions such that the likelihood is
    relatively flat within the remaining prior volume.

    Method:
    The trick in nested sampling is to, at each step in the algorithm,
    efficiently choose a new point in parameter space drawn with uniform
    probability from the parameter space with likelihood greater than the
    current likelihood constraint. The different methods all use the
    current set of active points as an indicator of where the target
    parameter space lies, but differ in how they select new points from  it.
    "classic" is close to the method described in Skilling (2004).
    "single", Mukherjee, Parkinson & Liddle (2006), Determines a single
    ellipsoid that bounds all active points,
    enlarges the ellipsoid by a user-settable factor, and selects a new point
    at random from within the ellipsoid.
    "multiple", Shaw, Bridges & Hobson (2007) and Feroz, Hobson & Bridges 2009
    (Multinest). In cases where the posterior is multi-modal,
    the single-ellipsoid method can be extremely inefficient: In such
    situations, there are clusters of active points on separate
    high-likelihood regions separated by regions of lower likelihood.
    Bounding all points in a single ellipsoid means that the ellipsoid
    includes the lower-likelihood regions we wish to avoid
    sampling from.
    The solution is to detect these clusters and bound them in separate
    ellipsoids. For this, we use a recursive process where we perform
    K-means clustering with K=2. If the resulting two ellipsoids have a
    significantly lower total volume than the parent ellipsoid (less than half),
    we accept the split and repeat the clustering and volume test on each of
    the two subset of points. This process continues recursively.
    Alternatively, if the total ellipse volume is significantly greater
    than expected (based on the expected density of points) this indicates
    that there may be more than two clusters and that K=2 was not an
    appropriate cluster division.
    We therefore still try to subdivide the clusters recursively. However,
    we still only accept the final split into N clusters if the total volume
    decrease is significant.

    """
    # ----------------------- Preparation/Formatting --------------------------

    nparams = len(init)
    
    if grid_param_list is not None:
        if model_grid is None and model_reader is None:
            msg = "Either model_grid or model_reader have to be provided"
            raise TypeError(msg)
        n_gparams = len(grid_param_list)
        gp_dims = []
        for nn in range(n_gparams):
            gp_dims.append(len(grid_param_list[nn]))
        gp_dims = tuple(gp_dims)
    else:
        n_gparams = 0
        
    # format emission line dictionary and em grid
    if len(em_grid)>0:
        n_em = len(em_grid)
        em_dims = []
        for lab in labels:
            if lab in em_grid.keys():
                em_dims.append(len(em_grid[lab]))
        em_dims = tuple(em_dims)
        # update the grids depending on input units => make it surface flux
        idx_R = labels.index('R')
        for key, val in em_lines.items():
            if val[1] == 'L':
                idx_line = labels.index(key)
                # adapt grid
                R_si = init[idx_R]*con.R_jup.value
                conv_fac = 4*np.pi*R_si**2
                tmp = np.array(em_grid[key])/conv_fac
                em_grid[key] = tmp.tolist()
                # adapt ini state 
                init = list(init)
                init[idx_line] /= conv_fac
                init = tuple(init)
                #adapt bounds
                bounds_ori = list(bounds[key])
                bounds[key] = (bounds_ori[0]/conv_fac, bounds_ori[1]/conv_fac) 
            elif val[1] == 'LogL':
                idx_line = labels.index(key)
                R_si = init[idx_R]*con.R_jup.value
                conv_fac = con.L_sun.value/(4*np.pi*R_si**2)
                tmp = np.power(10,np.array(em_grid[key]))*conv_fac
                em_grid[key] = tmp.tolist()  
                # adapt ini state 
                init = list(init)
                init[idx_line] = conv_fac*10**init[idx_line]
                init = tuple(init)
                #adapt bounds
                bounds_ori = list(bounds[key])
                bounds[key] = (conv_fac*10**bounds_ori[0], 
                               conv_fac*10**bounds_ori[1]) 
            if em_lines[key][2] is not None:
                if em_lines[key][-1] == 'km/s':
                    v = em_lines[key][2]
                    em_lines_tmp = list(em_lines[key])
                    em_lines_tmp[2] = (1000*v/con.c.value)*em_lines[key][0]
                    em_lines_tmp[3] = 'mu'
                    em_lines[key] = tuple(em_lines_tmp)
                elif em_lines[key][-1] == 'nm':
                    em_lines_tmp = list(em_lines[key])
                    em_lines_tmp[2] = em_lines[key][2]/1000
                    em_lines_tmp[3] = 'mu'
                    em_lines[key] = tuple(em_lines_tmp)
                elif em_lines[key][-1] != 'mu':
                    msg = "Invalid unit of FWHM for line injection"
                    raise ValueError(msg)
                
    if model_grid is not None and grid_param_list is not None:
        if model_grid.ndim-2 != n_gparams:
            msg = "Ndim-2 of model_grid should match len(grid_param_list)"
            raise TypeError(msg)

 
    # Check model grid parameters extend beyond bounds to avoid extrapolation
    if grid_param_list is not None:
        for pp in range(n_gparams):
            if grid_param_list[pp][0]>bounds[labels[pp]][0]:
                msg= "Grid has to extend beyond bounds for {}."
                msg+="\n Consider increasing the lower bound to >{}."
                raise ValueError(msg.format(labels[pp],grid_param_list[pp][0]))
            if grid_param_list[pp][-1]<bounds[labels[pp]][1]:
                msg= "Grid has to extend beyond bounds for {}."
                msg+="\n Consider decreasing the upper bound to <{}."
                raise ValueError(msg.format(labels[pp],grid_param_list[pp][1]))
                
    # Check initial state is within bounds for all params (not only grid)
    for pp in range(nparams):
        if init[pp]<bounds[labels[pp]][0]:
            msg= "Initial state has to be within bounds for {}."
            msg+="\n Consider decreasing the lower bound to <{}."
            raise ValueError(msg.format(labels[pp],init[pp]))            
        if init[pp]>bounds[labels[pp]][1]:
            msg= "Initial state has to be within bounds for {}."
            msg+="\n Consider decreasing the upper bound to >{}."
            raise ValueError(msg.format(labels[pp],init[pp]))
        
    # Prepare model grid: convolve+resample models as observations 
    if resamp_before and grid_param_list is not None:
        if isfile(output_dir+grid_name):
            model_grid = open_fits(output_dir+grid_name)
            # check its shape is consistent with grid_param_list
            if model_grid.shape[:n_gparams] != gp_dims:
                msg="the loaded model grid ({}) doesn't have expected dims ({})"
                raise TypeError(msg.format(model_grid.shape,gp_dims))
            elif model_grid.shape[-2] != len(lbda_obs):
                msg="the loaded model grid doesn't have expected WL dimension"
                raise TypeError(msg)
            elif model_grid.shape[-1] != 2:
                msg="the loaded model grid doesn't have expected last dimension"
                raise TypeError(msg)
            elif len(em_grid) > 0:
                if model_grid.shape[n_gparams:n_gparams+n_em] != em_dims:
                    msg="loaded model grid ({}) doesn't have expected dims ({})"
                    raise TypeError(msg.format(model_grid.shape,em_dims))
        else:
            model_grid = make_resampled_models(lbda_obs, grid_param_list, 
                                               model_grid, model_reader, 
                                               em_lines, em_grid, dlbda_obs, 
                                               instru_fwhm, instru_idx, 
                                               filter_reader, interp_nonexist)
            if output_dir and grid_name:
                write_fits(output_dir+grid_name, model_grid)
        # note: if model_grid is provided, it is still resampled to the 
        # same wavelengths as observed spectrum. However, if a fits name is 
        # provided in grid_name and that file exists, it is assumed the model 
        # grid in it is already resampled to match lbda_obs.    


    # -------------- Definition of utilities for nested sampling --------------

    def prior_transform(x):
        """
        Computes the transformation from the unit distribution `[0, 1]` to 
        parameter space. Uniform distributions are assumed for all parameters.
        
        
        Notes
        -----
        The prior transform function is used to specify the Bayesian prior for 
        the problem, in a round-about way. It is a transformation from a space 
        where variables are independently and uniformly distributed between 0 
        and 1 to the parameter space of interest. For independent parameters, 
        this would be the product of the inverse cumulative distribution 
        function (also known as the percent point function or quantile function) 
        for each parameter.
        http://kbarbary.github.io/nestle/prior.html
        """
        # uniform priors
        pt = []
        for p in range(nparams):            
            pmin = bounds[labels[p]][0]
            pmax = bounds[labels[p]][1]
            pt.append(x[p] * (pmax - pmin) + pmin)
                
        if priors is not None:
            # replace with Gaussian prior where relevant
            for key, prior in priors.items():
                if key == 'M' and 'logg' in labels:
                    msg = "Mass prior only available for MCMC sampling"
                    raise ValueError(msg)
                else:
                    idx_prior = labels.index(key)
                    pt[idx_prior] = prior[0] + prior[1] * ndtri(x)
            
        return np.array(pt)

    def f(param):
        
        return lnlike(param, labels, grid_param_list, lbda_obs, spec_obs, 
                      err_obs, dist, model_grid=model_grid,
                      model_reader=model_reader, em_lines=em_lines, 
                      em_grid=em_grid, dlbda_obs=dlbda_obs, 
                      instru_corr=instru_corr, instru_fwhm=instru_fwhm, 
                      instru_idx=instru_idx, filter_reader=filter_reader, 
                      AV_bef_bb=AV_bef_bb, units_obs=units_obs, 
                      units_mod=units_mod, interp_order=interp_order)
        
        
    # ------------------------ Actual sampling --------------------------------
    if verbose:  start = time_ini()

    if verbose:
        print('Prior bounds on parameters:')
        for p in range(nparams):            
            pmin = bounds[labels[p]][0]
            pmax = bounds[labels[p]][1]
            print('{} [{},{}]'.format(labels[p], pmin, pmax))
        print('\nUsing {} active points'.format(npoints))

    res = nestle.sample(f, prior_transform, ndim=nparams, method=method,
                        npoints=npoints, rstate=rstate, dlogz=dlogz,
                        decline_factor=decline_factor, **kwargs)

    if verbose:
        print('\nTotal running time:')
        timing(start)
        
    return res


def nested_sampling_results(ns_object, labels, burnin=0.4, bins=None, cfd=68.27,
                            units=None, ndig=None, labels_plot=None, save=False, 
                            output_dir='/', plot=False,  **kwargs):
    """ 
    Shows the results of the Nested Sampling, summary, parameters with 
    errors, walk and corner plots. Returns best-fit values and uncertatinties.
    
    Parameters
    ----------
    ns_object: numpy.array
        The nestle object returned from `nested_spec_sampling`.
    labels: Tuple of strings
        Tuple of labels in the same order as initial_state, that is:
        - first all parameters related to loaded models (e.g. 'Teff', 'logg')
        - then the planet photometric radius 'R', in Jupiter radius
        - (optionally) the flux of emission lines (labels should match those \
        in the em_lines dictionary), in units of the model spectrum (times mu)
        - (optionally) the optical extinction 'Av', in mag
        - (optionally) the ratio of total to selective optical extinction 'Rv'
        - (optionally) 'Tbb1', 'Rbb1', 'Tbb2', 'Rbb2', etc. for each extra bb \
        contribution. 
    burnin: float, default: 0
        The fraction of a walker we want to discard.
    bins: int, optional
        The number of bins used to sample the posterior distributions.
    cfd: float, optional
        The confidence level given in percentage.
    units: tuple, opt
        Tuple of strings containing units for each parameter. If provided,
        mcmc_res will be printed on top of each 1d posterior distribution along 
        with these units.
    ndig: tuple, opt
        Number of digits precision for each printed parameter
    labels_plot: tuple, opt
        Labels corresponding to parameter names, used for the plot. If None,
        will use "labels" passed in kwargs.
    save: boolean, default: False
        If True, a pdf file is created.
    output_dir: str, optional
        The name of the output directory which contains the output files in the 
        case  ``save`` is True. 
    plot: bool, optional
        Whether to show the plots (instead of saving them).
    kwargs:
        Additional optional arguments passed to `confidence` (matplotlib 
        optional arguments for histograms).
                    
    Returns
    -------
    final_res: numpy ndarray
         Best-fit parameters and uncertainties (corresponding to 68% confidence
         interval). Dimensions: nparams x 2.
    
    """
    res = ns_object
    nsamples = res.samples.shape[0]
    indburnin = int(np.percentile(np.array(range(nsamples)), burnin * 100))
    nparams = len(labels)

    print(res.summary())

    print(
        '\nNatural log of prior volume and Weight corresponding to each sample')
    if save or plot:
        plt.figure(figsize=(12, 4))
        plt.subplot(1, 2, 1)
        plt.plot(res.logvol, '.', alpha=0.5, color='gray')
        plt.xlabel('samples')
        plt.ylabel('logvol')
        plt.vlines(indburnin, res.logvol.min(), res.logvol.max(),
                   linestyles='dotted')
        plt.subplot(1, 2, 2)
        plt.plot(res.weights, '.', alpha=0.5, color='gray')
        plt.xlabel('samples')
        plt.ylabel('weights')
        plt.vlines(indburnin, res.weights.min(), res.weights.max(),
                   linestyles='dotted')
        if save:
            plt.savefig(output_dir+'Nested_results.pdf')
        if plot:
            plt.show()
            
        print("\nWalk plots before the burnin")
        show_walk_plot(np.expand_dims(res.samples, axis=0), labels)
        if burnin > 0:
            print("\nWalk plots after the burnin")
            show_walk_plot(np.expand_dims(res.samples[indburnin:], axis=0),
                           labels)
        if save:
            plt.savefig(output_dir+'Nested_walk_plots.pdf')
        
    mean, cov = nestle.mean_and_cov(res.samples[indburnin:],
                                    res.weights[indburnin:])
    print("\nWeighted mean +- sqrt(covariance)")
    if ndig is None:
        ndig = [3]*len(labels)   
    for p in range(nparams):
        fmt = "{{:.{0}f}}".format(ndig[p]).format
        print(r"{0} = {1} +/- {2}".format(labels[p], fmt(mean[p]), 
                                          fmt(np.sqrt(cov[p, p]))))
    if save:
        with open(output_dir+'Nested_sampling.txt', "w") as f:
            f.write('#################################\n')
            f.write('####   CONFIDENCE INTERVALS   ###\n')
            f.write('#################################\n')
            f.write(' \n')
            f.write('Results of the NESTED SAMPLING fit\n')
            f.write('----------------------------------\n ')
            f.write(' \n')
            f.write("\nWeighted mean +- sqrt(covariance)\n")
            for p in range(nparams):
                fmt = "{{:.{0}f}}".format(ndig[p]).format
                f.write(r"{0} = {1} +/- {2}\n".format(labels[p], fmt(mean[p]), 
                                                      fmt(np.sqrt(cov[p, p]))))
                        
    final_res = np.zeros([nparams,2]) 
    for p in range(nparams):     
        final_res[p] = [mean[p], np.sqrt(cov[p, p])]

    if bins is None:
        bins = int(np.sqrt(res.samples[indburnin:].shape[0]))
        print("\nHist bins =", bins)
    
    if save or plot:
        show_corner_plot(res.samples[indburnin:], burnin=burnin, save=save, 
                         output_dir=output_dir, mcmc_res=final_res, units=units, 
                         ndig=ndig, labels_plot=labels_plot, 
                         plot_name='corner_plot.pdf', labels=labels)
    if save:
        plt.savefig(output_dir+'Nested_corner.pdf')
    if plot:
        plt.show()
            
    print('\nConfidence intervals')
    if save or plot:
        _ = confidence(res.samples[indburnin:], labels, cfd=cfd, bins=bins,
                       weights=res.weights[indburnin:],
                       gaussian_fit=True, verbose=True, save=False, **kwargs)        
     
    if save:
        plt.savefig(output_dir+'Nested_confi_hist_flux_r_theta_gaussfit.pdf')

    if plot:
        plt.show()
        
    return final_res