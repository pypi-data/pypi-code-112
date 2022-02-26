from setuptools import setup, find_packages

setup(
    name='medusa-kernel',
    packages=find_packages(),
    version='0.1',
    description='Advanced biosignal processing toolbox',
    keywords=['Signal', 'Biosignal', 'EEG', 'BCI'],
    url='https://gib.tel.uva.es/',
    download_url='https://github.com/gib-uva/medusa-kernel/'
                 'archive/refs/tags/v0.1.tar.gz',
    author='Eduardo Santamaría-Vázquez, '
           'Víctor Martínez-Cagigal, '
           'Víctor Rodríguez-González',
    author_email='eduardo.santamaria@gib.tel.uva.es',
    license='MIT',
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'numba',
        'sklearn',
        'statsmodels',
        'bson',
        'h5py',
        'dill',
        'tqdm'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
