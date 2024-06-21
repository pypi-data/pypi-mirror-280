# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['project001', 'project001.pkg1']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.32.3,<3.0.0']

setup_kwargs = {
    'name': 'project001',
    'version': '0.2.0',
    'description': 'project001 is used for simple test',
    'long_description': '### this is project001\n',
    'author': 'johnypeng',
    'author_email': '2651903873@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
