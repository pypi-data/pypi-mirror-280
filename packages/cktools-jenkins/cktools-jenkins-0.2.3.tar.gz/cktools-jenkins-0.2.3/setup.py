# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cktools_jenkins']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['ckgitinfo = cktools_jenkins.git_src_info_extractor:main',
                     'ckmail = cktools_jenkins.send_email:main']}

setup_kwargs = {
    'name': 'cktools-jenkins',
    'version': '0.2.3',
    'description': 'Tools for Jenkins',
    'long_description': '# CKTools-Jenkins v0.2.3',
    'author': 'Chandan Kumar',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=2.7,<3.0',
}


setup(**setup_kwargs)
