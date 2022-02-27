# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tablespoon']

package_data = \
{'': ['*'],
 'tablespoon': ['stan/mean.stan',
                'stan/mean.stan',
                'stan/mean.stan',
                'stan/mean.stan',
                'stan/naive.stan',
                'stan/naive.stan',
                'stan/naive.stan',
                'stan/naive.stan',
                'stan/snaive.stan',
                'stan/snaive.stan',
                'stan/snaive.stan',
                'stan/snaive.stan',
                'stan/snaive_t_dist.stan',
                'stan/snaive_t_dist.stan',
                'stan/snaive_t_dist.stan',
                'stan/snaive_t_dist.stan']}

install_requires = \
['cmdstanpy>=0.9.77,<0.10.0',
 'numpy>=1.21.2,<2.0.0',
 'pandas>=1.3.2,<2.0.0',
 'pytest>=6.2.5,<7.0.0']

setup_kwargs = {
    'name': 'tablespoon',
    'version': '0.1.24',
    'description': 'Simple probabilistic time series benchmark models',
    'long_description': '[![Python application](https://github.com/alexhallam/tablespoon/actions/workflows/python-app.yml/badge.svg)](https://github.com/alexhallam/tablespoon/actions/workflows/python-app.yml)\n\n<h1 align="center">tablespoon</h1>\n<p align="center"><b>T</b>ime-series <b>B</b>enchmark methods that are <b>S</b>imple and <b>P</b>robabilistic</p>\n\n<p align="center"><img align="center" src="assets/tbsp.png" width="300" /></p>\n\n\n# Documentation and quick links\n* [Introduction](#introduction)\n* [Quick Example](#quick-example)\n* [Why Run Simple Methods](#why-run-simple-methods)\n* [Goals of this package](#goals-of-this-package)\n* [Non-Goals](#non-goals)\n* [Forecast Method Documentation](docs/FORECAST_METHODS.md)\n* [Installation](#installation)\n* [Recommended probabilistic forecasting packages](#recommended-probabilistic-forecasting-packages)\n* [Learn more about forecasting](#learn-more-about-forecasting)\n\n# Introduction\n\nMany methods exist for probabilistic forecasting. If you are looking for an\nimpressive probabilistic forecasting package see the list of recommendation at\nthe bottom of this README. This package is <b>exceptionally ordinary</b>. It is\nexpected that this package may be used as a compliment to what is already out\nthere.\n\n# Why Run Simple Methods\n\nWe have found, by experience, many good uses for the methods in this package.\nTo often we see that forecast methods go in production without a naive method to\naccompany it. This is a missed opportunity.\n\n1. **Naive May Be Good Enough**: Some applications do not need anything more\n   impressive than a simple forecasting method.\n2. **Get A Denominator for Relative Metrics**: Though naive methods can usually\n   be beat it is good to know the relative improvement over the benchmark. This\n   can allow a forecasting team to market their alternative forecast when the\n   \'skill score\' is impressive.\n3. **Easy to productionize and get expectations**: Get a sense for how good is\n   good enough. In many applications a forecast team is asked to forecast, but\n   stakeholders provide no line-in-the-sand for when the forecasting work needs\n   to stop. One reasonable approach is to run the benchmarks found in this\n   package in beat the best performing benchmark by a margin that is\n   statistically significant.\n4. **Resilience in Production - Why not have many models?**: Sometimes, despite\n   out best efforts our production model does something unexpected. In this\n   case it is nice to have a simple backup that is cheap to generate and good\n   enough to fall back on. In this way a production forecast pipeline gains\n   strength from a diversity of models.\n5. **Easy Uncertainty Quantification**: More and more we see that application\n   are not about forecast accuracy, but instead about forecasting uncertainty.\n   Capturing the full distribution helps firms set "service levels" aka\n   percentiles of the distribution for which they are prepared to serve. Even\n   if you have the worlds most accurate unbiased forecast the median point is\n   an underforecast half the time. For this reason it is best to provide a\n   distribution of simulated future values and the firm may decide for\n   themselves what risks they are or are not willing to take.\n\n# Quick Example\n\nWe show a quick example below. For more examples see [EXAMPLES.md](docs/EXAMPLES.md)\n\n```python\nimport tablespoon as tbsp\nfrom tablespoon.data import APPL\n\n# Uncomment if this is your first time installing cmdstanpy\n# from cmdstanpy import install_cmdstan\n# install_cmdstan()\n\nn = tbsp.Naive()\ndf_n = n.predict(\n    APPL, horizon=7 * 4, frequency="D", lag=1, uncertainty_samples=8000\n).assign(model="naive")\n\nprint(df_n.head(10))\n```\n\n```sh\n          ds  rep    y_sim  model\n0 2022-01-02    0  5.20006  naive\n1 2022-01-02    1  5.16789  naive\n2 2022-01-02    2  5.17641  naive\n3 2022-01-02    3  5.19340  naive\n4 2022-01-02    4  5.20075  naive\n5 2022-01-02    5  5.17681  naive\n6 2022-01-02    6  5.20302  naive\n7 2022-01-02    7  5.18896  naive\n8 2022-01-02    8  5.19622  naive\n9 2022-01-02    9  5.17469  naive\n```\n<p align="center"><img align="center" src="assets/forecasts_n.jpg" width="800" /></p>\n\n\n\n# Goals of this package\n\n1. ♙**Simple**: Not just in the forecasts themselves, but also from the\n   users perspective.\n2. ♝**Documented**: It should be very clear exactly how forecasts are getting\n   generated. We document the parameterization of the models to make this as\n   obvious and uninteresting as possible. See [Forecast Method Documentation](docs/FORECAST_METHODS.md)\n3. ♜**Stable**: We want this package to feel rock solid. For this to happen\n   we keep the feature set relatively small. We believe that after the initial \n   development of this package we should spend out time maintaining the code as\n   oppose to thinking of new features.\n4. ♞**Distributional**: Quantification of uncertainty is the name of\n   the game. Because this uses [Stan](https://mc-stan.org/) in the backend users get access to state of\n   of the art numerical sampling.\n3. ♛**Accessible**: Because of how important we feel simple forecasting\n   methods are we want as many front end binding as possible to expose these\n   methods to the largest audience possible. We eventually have binding in\n   `Shell`,`Julia`,`R`, and `Python. (This will come with time)\n\n# Non-Goals\n\n1. 🔥**Circut Melting Focus on Speed**: Not to say this is a slow package. In fact, all\n   models do get compiled. It is very fast! We just don\'t put any extra effort to make \n   it faster than the `C++` Stan compiled model.\n2. 🤖**New/Complex Forecast Models**: Again, this is out of scope. If you are\n   looking for recommendations please see the bottom of the page.\n\n# Installation\n\n### Python\n\n```\npip3 install tablespoon\n```\n\n# Citation\n\nIf you would like to cite `tablespoon`, please cite it as follows:\n\nAlex Hallam. **tablespoon: Time-series Benchmark methods that are Simple and Probabilistic** https://github.com/alexhallam/tablespoon, 2021. Version 0.1.6.\n\n```\n@misc{tablespoon,\n  author={Alex Hallam},\n  title={{tablespoon}: {Time-series Benchmark methods that are Simple and Probabilistic},\n  howpublished={https://github.com/alexhallam/tablespoon},\n  note={Version 0.1.8,\n  year={2021}\n}\n```\n\n# References\n\n1. Hyndman, R.J., & Athanasopoulos, G. (2021) Forecasting: principles and practice, 3rd edition, OTexts: Melbourne, Australia. OTexts.com/fpp3. Accessed on 2021-09-26.\n2. Stan Development Team. 2021. Stan Modeling Language Users Guide and Reference Manual, 2.27.0. https://mc-stan.org\n\n# Recommended probabilistic forecasting packages\n\nThere are many packages that can compliment `tablespoon`\n\n[forecast](https://github.com/robjhyndman/forecast): The king of forecasting\npackages. Rob Hyndman is a professor of forecasting and has served as editor of\nthe journal "International Journal of Forecasting". If you are new to\nforecasting please read his free ebook [fpp3](https://otexts.com/fpp3/).\n\n[prophet](https://facebook.github.io/prophet/): A very capable and reliable\nforecasting package. I have never seen a bad forecast come out of prophet.\n\n[gluonts](https://ts.gluon.ai/). If you are itching to use neural nets for\nforecasting this is a good one to pick.\n\n# Learn more about forecasting\n\n1. Read [fpp3](https://otexts.com/fpp3/)\n2. Join the [International Institute of Forecasting](https://forecasters.org/)\n   and read their publications.\n\n# Beta\n\nThis package is currently being tested. It is very much unfinished at this point.\nFeel free to use what is currently available. \n\n# Built with poetry and pushed to pypi\n\n```sh\npoetry publish -u <username> -p <password> --build\n```\n',
    'author': 'Alex Hallam',
    'author_email': 'alexhallam6.28@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/alexhallam/tablespoon',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)
