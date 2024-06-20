# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src/py'}

packages = \
['daisyflcocdrlib',
 'daisyflcocdrlib.client',
 'daisyflcocdrlib.client.grpc_client',
 'daisyflcocdrlib.client.grpc_server',
 'daisyflcocdrlib.common',
 'daisyflcocdrlib.master',
 'daisyflcocdrlib.master.grpc_server',
 'daisyflcocdrlib.operator',
 'daisyflcocdrlib.operator.base',
 'daisyflcocdrlib.operator.base_async',
 'daisyflcocdrlib.operator.msg_demo',
 'daisyflcocdrlib.operator.sec_agg',
 'daisyflcocdrlib.operator.strategy',
 'daisyflcocdrlib.operator.utils',
 'daisyflcocdrlib.proto',
 'daisyflcocdrlib.simulation',
 'daisyflcocdrlib.simulation.ray_transport',
 'daisyflcocdrlib.utils',
 'daisyflcocdrlib.zone',
 'daisyflcocdrlib.zone.grpc_client',
 'daisyflcocdrlib.zone.grpc_server']

package_data = \
{'': ['*']}

install_requires = \
['Flask>=2.2.2,<3.0.0',
 'cryptography>=38.0.4,<39.0.0',
 'dataclasses-json>=0.5.7,<0.6.0',
 'grpcio>=1.43.0,<2.0.0',
 'iterators>=0.0.2,<0.0.3',
 'numpy>=1.21.0,<2.0.0',
 'protobuf>=3.19.0,<4.0.0',
 'pycryptodome>=3.16.0,<4.0.0']

extras_require = \
{':python_version < "3.8"': ['importlib-metadata>=4.0.0,<5.0.0'],
 'simulation': ['ray[default]>=2.0.0,<2.1.0']}

setup_kwargs = {
    'name': 'daisyflcocdrlib',
    'version': '0.0.6',
    'description': 'Daisy - A Hierarchical Friendly Federated Learning Framework For Edge Computing',
    'long_description': "# Daisy - A Hierarchical Friendly Federated Learning Framework For Edge Computing\n\n\n## dev mode (virtual environment)\n### 1. clone the source code\n```\ngit clone https://github.com/Intelligent-Systems-Lab/daisy\n```\n### 2. build up environment\nprepare and activate your virtual environment (python=3.8^)\n```\ncd daisy\n./dev/bootstrap.sh\n```\n### develop<br>\n### setup examples\ndon't overwrite daisyflcocdrlib dependency in this step.<br>\n```\ncd <example_path>\npip install <pkgs_for_your_example>\n```\n### 5. run examples\n\n## dev mode (docker)\n### 1. clone the source code\n```\ngit clone https://github.com/Intelligent-Systems-Lab/daisy\n```\n### 2. build up environment\n```\ndocker run -it -v <daisy_source_code>:/root/daisy tcfwbper/daisyflcocdrlib-dev:<version_tag> /bin/bash\n```\n### 3. develop<br>\n### 4. setup examples<br>\ndon't overwrite daisyflcocdrlib dependency in this step.<br>\n```\ndocker attach <container_id>\n```\n```\ncd <example_path> && conda activate daisy\npip install <pkgs_for_your_example>\n```\n### 5. run examples\n\n## user mode\n### 1. install daisyflcocdrlib\n```\npip install <daisyflcocdrlib_version>\n```\n### 2. setup examples\n```\npip install <pkgs_for_your_example>\n```\n### 3. run examples",
    'author': 'qmooo',
    'author_email': 'zoh92117@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Intelligent-Systems-Lab/daisy',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
