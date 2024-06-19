# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['debtcmining']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp-proxy==0.1.2',
 'aiohttp==3.9.5',
 'colorama==0.4.6',
 'loguru==0.7.2',
 'pydantic==2.7.4',
 'sqlalchemy==2.0.30']

setup_kwargs = {
    'name': 'debtcmining',
    'version': '0.0.1rc4',
    'description': '',
    'long_description': '',
    'author': 'DesKaOne',
    'author_email': 'DesKaOne@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
