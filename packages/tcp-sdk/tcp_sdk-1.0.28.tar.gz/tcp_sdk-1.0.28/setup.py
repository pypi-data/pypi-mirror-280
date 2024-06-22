# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['tcp']

package_data = \
{'': ['*']}

install_requires = \
['pyzmq==25.1.2',
 'requests-oauthlib>=2.0.0,<3.0.0',
 'requests>=2.31.0,<3.0.0',
 'slumber>=0.7.1,<0.8.0']

extras_require = \
{'ipython': ['ipython>=8.24.0,<9.0.0']}

setup_kwargs = {
    'name': 'tcp-sdk',
    'version': '1.0.28',
    'description': 'Python SDK to query The Cross Product API.',
    'long_description': '\nTCP python SDK \n==============\n\ntcp-sdk is a Python module that provides a convenient object-oriented interface to TCP API. It acts as a wrapper around [slumber](https://github.com/samgiles/slumber).\n\nQuickStart\n----------\n\n* Install *tcp-sdk*\n\n\n      $ virtualenv my_virtualenv\n      $ source my_virtualenv/bin/activate\n      $ pip install tcp-sdk\n\n* Connect to your TCP account\n\n      import tcp\n      client = tcp.client (usermail="user@domain.org", passwd="passwd")\n      print(client.token)\n\n  \nSave this token to the environment variable `$TCP_API_TOKEN`.\nLatter calls to ``tcp.client()`` will automatically connect to TCP API using this environment variable.\n\n* Start using tcp-sdk\n\n      import tcp\n      client = tcp.client ()\n      print (client.query().auth.get())\n\nRequirements\n------------\n\n*tcp-sdk* requires the following modules.\n\n * *requests*\n * *slumber*\n * *requests-oauthlib*\n\n\n',
    'author': 'Théodore Chabardès',
    'author_email': 'theodore.chabardes@thecrossproduct.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
