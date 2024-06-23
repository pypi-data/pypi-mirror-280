# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aws_jmespath_utils']

package_data = \
{'': ['*']}

install_requires = \
['jmespath>=1.0.1,<2.0.0']

setup_kwargs = {
    'name': 'aws-jmespath-utils',
    'version': '0.1.11',
    'description': 'jmespath custom functions for filtering AWS resources by tag',
    'long_description': '# aws-jmespath-utils\n\n## Installation\n\n```bash\npip3 install aws_jmespath_utils\n```\n\n## Usage\n\n```python\njmespath.search(  # it\'s important that your expression array must be inside `` backticks\n    \'[] | filter_tags(`["Name=*"]`, @)\', data_list, options=jmespath_options\n)\n```\n\n```python\njmespath.search(  # it\'s important that your expression array must be inside `` backticks\n    \'[] | filter_tags(`["[!Name]="]`, @)\', data_list, options=jmespath_options\n)\n\n```\n\n\n```bash\n# set log level as you wish\nexport AWS_JMESPATH_UTILS_LOG_LEVEL="DEBUG"   \nexport AWS_JMESPATH_UTILS_LOG_LEVEL="WARNING"   \nexport AWS_JMESPATH_UTILS_LOG_LEVEL="INFO"  # default   \n```\n\n',
    'author': 'Oguzhan Yilmaz',
    'author_email': 'oguzhanylmz271@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
