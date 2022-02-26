import pycaret.internal.patches.sklearn
import pycaret.internal.patches.yellowbrick
from pycaret.internal.logging import get_logger
from pycaret.internal.distributions import *
from pycaret.internal.validation import *
import pycaret.internal.preprocess
import pycaret.internal.persistence
import pandas as pd  # type ignore
import numpy as np  # type: ignore
from typing import List, Tuple, Any, Union, Optional, Dict
import warnings
import plotly.express as px  # type: ignore
import plotly.graph_objects as go  # type: ignore


warnings.filterwarnings("ignore")
LOGGER = get_logger()


class _PyCaretExperiment:
    def __init__(self) -> None:
        self._ml_usecase = None
        self._available_plots = {}
        self.variable_keys = set()
        self._setup_ran = False
        self.display_container = []
        self.exp_id = None
        self.gpu_param = False
        self.n_jobs_param = -1
        self.logger = LOGGER
        return

    @property
    def _gpu_n_jobs_param(self) -> int:
        return self.n_jobs_param if not self.gpu_param else 1

    @property
    def variables(self) -> dict:
        return {
            k: (vars(self)[k] if k in vars(self) else None) for k in self.variable_keys
        }

    def _is_multiclass(self) -> bool:
        """
        Method to check if the problem is multiclass.
        """
        return False

    def _check_enviroment(self) -> None:
        # logging environment and libraries
        self.logger.info("Checking environment")

        from platform import python_version, platform, python_build, machine

        self.logger.info(f"python_version: {python_version()}")
        self.logger.info(f"python_build: {python_build()}")
        self.logger.info(f"machine: {machine()}")
        self.logger.info(f"platform: {platform()}")

        try:
            import psutil

            self.logger.info(f"Memory: {psutil.virtual_memory()}")
            self.logger.info(f"Physical Core: {psutil.cpu_count(logical=False)}")
            self.logger.info(f"Logical Core: {psutil.cpu_count(logical=True)}")
        except Exception:
            self.logger.warning(
                "cannot find psutil installation. memory not traceable. Install psutil using pip to enable memory logging."
            )

        self.logger.info("Checking libraries")

        try:
            from pandas import __version__

            self.logger.info(f"pd=={__version__}")
        except ImportError:
            self.logger.warning("pandas not found")

        try:
            from numpy import __version__

            self.logger.info(f"numpy=={__version__}")
        except ImportError:
            self.logger.warning("numpy not found")

        try:
            from sklearn import __version__

            self.logger.info(f"sklearn=={__version__}")
        except ImportError:
            self.logger.warning("sklearn not found")

        try:
            from lightgbm import __version__

            self.logger.info(f"lightgbm=={__version__}")
        except ImportError:
            self.logger.warning("lightgbm not found")

        try:
            from xgboost import __version__

            self.logger.info(f"xgboost=={__version__}")
        except ImportError:
            self.logger.warning("xgboost not found")

        try:
            from catboost import __version__

            self.logger.info(f"catboost=={__version__}")
        except ImportError:
            self.logger.warning("catboost not found")

        try:
            from mlflow.version import VERSION

            warnings.filterwarnings("ignore")
            self.logger.info(f"mlflow=={VERSION}")
        except ImportError:
            self.logger.warning("mlflow not found")

    def setup(self, *args, **kwargs) -> None:
        return

    def deploy_model(
        self,
        model,
        model_name: str,
        authentication: dict,
        platform: str = "aws",  # added gcp and azure support in pycaret==2.1
    ):
        return None

    def save_model(
        self,
        model,
        model_name: str,
        model_only: bool = False,
        verbose: bool = True,
        **kwargs,
    ):
        return None

    def load_model(
        self,
        model_name,
        platform: Optional[str] = None,
        authentication: Optional[Dict[str, str]] = None,
        verbose: bool = True,
    ):

        """
        This function loads a previously saved transformation pipeline and model
        from the current active directory into the current python environment.
        Load object must be a pickle file.

        Example
        -------
        >>> saved_lr = load_model('lr_model_23122019')

        This will load the previously saved model in saved_lr variable. The file
        must be in the current directory.

        Parameters
        ----------
        model_name : str, default = none
            Name of pickle file to be passed as a string.

        platform: str, default = None
            Name of platform, if loading model from cloud. Current available options are:
            'aws', 'gcp' and 'azure'.

        authentication : dict
            dictionary of applicable authentication tokens.

            When platform = 'aws':
            {'bucket' : 'Name of Bucket on S3'}

            When platform = 'gcp':
            {'project': 'gcp_pycaret', 'bucket' : 'pycaret-test'}

            When platform = 'azure':
            {'container': 'pycaret-test'}

        verbose: bool, default = True
            Success message is not printed when verbose is set to False.

        Returns
        -------
        Model Object

        """

        return pycaret.internal.persistence.load_model(
            model_name, platform, authentication, verbose
        )

    def get_logs(
        self, experiment_name: Optional[str] = None, save: bool = False
    ) -> pd.DataFrame:

        """
        Returns a table with experiment logs consisting
        run details, parameter, metrics and tags.

        Example
        -------
        >>> logs = get_logs()

        This will return pandas dataframe.

        Parameters
        ----------
        experiment_name : str, default = None
            When set to None current active run is used.

        save : bool, default = False
            When set to True, csv file is saved in current directory.

        Returns
        -------
        pandas.DataFrame

        """

        import mlflow
        from mlflow.tracking import MlflowClient

        client = MlflowClient()

        if experiment_name is None:
            exp_id = self.exp_id
            experiment = client.get_experiment(exp_id)
            if experiment is None:
                raise ValueError(
                    "No active run found. Check logging parameter in setup or to get logs for inactive run pass experiment_name."
                )

            exp_name_log_ = experiment.name
        else:
            exp_name_log_ = experiment_name
            experiment = client.get_experiment_by_name(exp_name_log_)
            if experiment is None:
                raise ValueError(
                    "No active run found. Check logging parameter in setup or to get logs for inactive run pass experiment_name."
                )

            exp_id = client.get_experiment_by_name(exp_name_log_).experiment_id

        runs = mlflow.search_runs(exp_id)

        if save:
            file_name = f"{exp_name_log_}_logs.csv"
            runs.to_csv(file_name, index=False)

        return runs

    def get_config(self, variable: str) -> Any:
        """
        This function is used to access global environment variables.

        Example
        -------
        >>> X_train = get_config('X_train')

        This will return X_train transformed dataset.

        Returns
        -------
        variable

        """

        function_params_str = ", ".join(
            [f"{k}={v}" for k, v in locals().items() if not k == "globals_d"]
        )

        self.logger.info("Initializing get_config()")
        self.logger.info(f"get_config({function_params_str})")

        if variable not in self.variables:
            raise ValueError(
                f"Variable {variable} not found. Possible variables are: {list(self.variables)}"
            )
        var = getattr(self, variable)

        self.logger.info(f"Variable: {variable} returned as {var}")
        self.logger.info(
            "get_config() succesfully completed......................................"
        )

        return var

    def set_config(
        self, variable: Optional[str] = None, value: Optional[Any] = None, **kwargs
    ) -> None:
        """
        This function is used to reset global environment variables.

        Example
        -------
        >>> set_config('seed', 123)

        This will set the global seed to '123'.

        """
        function_params_str = ", ".join(
            [f"{k}={v}" for k, v in locals().items() if not k == "globals_d"]
        )

        self.logger.info("Initializing set_config()")
        self.logger.info(f"set_config({function_params_str})")

        if kwargs and variable:
            raise ValueError(
                "variable parameter cannot be used together with keyword arguments."
            )

        variables = kwargs if kwargs else {variable: value}

        for k, v in variables.items():
            if k.startswith("_"):
                raise ValueError(f"Variable {k} is read only ('_' prefix).")

            if k not in self.variables:
                raise ValueError(
                    f"Variable {k} not found. Possible variables are: {list(self.variables)}"
                )

            setattr(self, k, v)
            self.logger.info(f"Global variable: {k} updated to {v}")
        self.logger.info(
            "set_config() succesfully completed......................................"
        )
        return

    def save_config(self, file_name: str) -> None:
        function_params_str = ", ".join(
            [f"{k}={v}" for k, v in locals().items() if not k == "globals_d"]
        )

        self.logger.info("Initializing save_config()")
        self.logger.info(f"save_config({function_params_str})")

        globals_to_ignore = {
            "_all_models",
            "_all_models_internal",
            "_all_metrics",
            "master_model_container",
            "display_container",
        }

        globals_to_dump = {
            k: v for k, v in self.variables.items() if k not in globals_to_ignore
        }

        import joblib

        joblib.dump(globals_to_dump, file_name)

        self.logger.info(f"Global variables dumped to {file_name}")
        self.logger.info(
            "save_config() succesfully completed......................................"
        )
        return

    def load_config(self, file_name: str) -> None:
        function_params_str = ", ".join(
            [f"{k}={v}" for k, v in locals().items() if not k == "globals_d"]
        )

        self.logger.info("Initializing load_config()")
        self.logger.info(f"load_config({function_params_str})")

        import joblib

        loaded_globals = joblib.load(file_name)

        self.logger.info(f"Global variables loaded from {file_name}")

        for k, v in loaded_globals.items():
            setattr(self, k, v)
            self.logger.info(f"Global variable: {k} updated to {v}")

        self.logger.info(f"Global variables set to match those in {file_name}")

        self.logger.info(
            "load_config() succesfully completed......................................"
        )
        return

    def pull(self, pop=False) -> pd.DataFrame:  # added in pycaret==2.2.0
        """
        Returns latest displayed table.

        Parameters
        ----------
        pop : bool, default = False
            If true, will pop (remove) the returned dataframe from the
            display container.

        Returns
        -------
        pandas.DataFrame
            Equivalent to get_config('display_container')[-1]

        """
        if not self.display_container:
            return None
        return self.display_container.pop(-1) if pop else self.display_container[-1]

