# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['subgrounds',
 'subgrounds.client',
 'subgrounds.contrib.dash',
 'subgrounds.contrib.plotly',
 'subgrounds.pagination',
 'subgrounds.subgraph',
 'subgrounds.transform']

package_data = \
{'': ['*'], 'subgrounds': ['contrib/*', 'resources/*']}

install_requires = \
['httpx[http2]>=0.25.1,<0.26.0',
 'pandas>=2.1,<3.0',
 'pipe>=2.0,<3.0',
 'pydantic>=2.0,<3.0',
 'pytest-asyncio']

extras_require = \
{'all': ['dash>=2.3.1,<3.0.0', 'plotly>=5.14.1,<6.0.0'],
 'dash': ['dash>=2.3.1,<3.0.0'],
 'plotly': ['plotly>=5.14.1,<6.0.0']}

setup_kwargs = {
    'name': 'subgrounds',
    'version': '1.9.1',
    'description': 'A Pythonic data access layer for applications querying data from The Graph Network.',
    'long_description': '# Subgrounds\n<!-- [![GitHub Actions](https://github.com/0xPlaygrounds/subgrounds/workflows/CI/badge.svg)](https://github.com/0xPlaygrounds/subgrounds/actions) -->\n[![PyPI](https://img.shields.io/pypi/v/subgrounds.svg)](https://pypi.org/project/subgrounds/)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/subgrounds.svg)](https://pypi.org/project/subgrounds/)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)\n[![CI](https://github.com/0xPlaygrounds/subgrounds/actions/workflows/main.yml/badge.svg)](https://github.com/0xPlaygrounds/subgrounds/actions/workflows/main.yml)\n<br>\n\n[![Discord](https://img.shields.io/discord/896944341598208070?color=7289DA&label=discord&logo=discord&logoColor=fff)](https://discord.gg/gMSSh5bjvk)\n[![Twitter Follow](https://img.shields.io/badge/Playgrounds-Analytics-31fa1f2Playgrounds0x?color=%231fa1f2&logo=Twitter&logoColor=1fa1f2&style=flat)](https://twitter.com/Playgrounds0x)\n\n[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/0xPlaygrounds/subgrounds/blob/main/examples/notebook.ipynb)\n[![Github Codepsaces](https://img.shields.io/badge/Github-Codespaces-24292f.svg?logo=Github)](https://codespaces.new/0xPlaygrounds/subgrounds-template?quickstart=1)\n\n<!-- start elevator-pitch -->\nAn intuitive Python library for interfacing with subgraphs and GraphQL.\n\n## Features\n- **Simple**: Leverage a Pythonic API to easily build queries and transformations without the need for raw GraphQL manipulation.\n- **Automated**: Automatically handle pagination and schema introspection for effortless data retrieval.\n- **Powerful**: Create sophisticated queries using the `SyntheticFields` transformation system.\n<!-- end elevator-pitch -->\n\n## Resources\n- [**Docs**](http://docs.playgrounds.network/): User guide and API documentation\n- [**Snippets**](https://github.com/0xPlaygrounds/subgrounds/tree/main/examples): A list of examples showcasing Subgrounds integration with Dash and Plotly\n- [**Examples**](http://docs.playgrounds.network/subgrounds/examples/): An ever growing list of projects created by our community members and team\n- [**Videos**](https://docs.playgrounds.network/subgrounds/videos/): Video workshops on Subgrounds\n\n## Installation\n> Subgrounds **requires** atleast Python 3.10+\n\nSubgrounds is available on PyPi. To install it, run the following:<br>\n`pip install subgrounds`.\n\nSubgrounds also comes bundled with extra modules that may require extra libraries. You can get all functionality of `subgrounds` via the following:<br>\n`pip install subgrounds[all]`.\n\n## Simple example\n<!-- start simple-example -->\n```python\n>>> from subgrounds import Subgrounds\n\n>>> sg = Subgrounds()\n\n>>> # Load\n>>> aave_v3 = sg.load_subgraph("https://api.thegraph.com/subgraphs/name/messari/aave-v3-ethereum")\n\n>>> # Construct the query\n>>> largest_markets = aave_v3.Query.markets(\n...     orderBy=aave_v3.Market.totalValueLockedUSD,\n...     orderDirection=\'desc\',\n...     first=5,\n... )\n\n>>> # Return query to a dataframe\n>>> sg.query_df([\n...     largest_markets.name,\n...     largest_markets.totalValueLockedUSD,\n... ])\n          markets_name  markets_totalValueLockedUSD\n0 Aave Ethereum wstETH                 1.915090e+09\n1   Aave Ethereum WETH                 1.047417e+09\n2   Aave Ethereum WBTC                 6.049655e+08\n3   Aave Ethereum USDC                 4.482461e+08\n4   Aave Ethereum USDT                 4.280103e+08\n```\n<!-- end simple-example -->\n\n\n## About Us\nPlaygrounds Analytics is a data solutions company providing data infrastructures and services for data teams, analysts, and engineers. Check us out [here](https://playgrounds.network/) to learn more!\n\n\n## Acknowledgments\nThis software project would not be possible without the support of The Graph Foundation. You can learn more about The Graph and its mission [here](https://thegraph.com/).\n',
    'author': 'cvauclair',
    'author_email': 'cvauclair@playgrounds.network',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/0xPlaygrounds/subgrounds',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
