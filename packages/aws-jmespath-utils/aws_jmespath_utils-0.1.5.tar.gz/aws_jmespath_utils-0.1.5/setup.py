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
    'version': '0.1.5',
    'description': 'jmespath custom functions for filtering AWS resources by tag',
    'long_description': '# aws-jmespath-utils\n\n## Installation\n\n```bash\npip3 install aws_jmespath_utils\n```\n\n## Usage\n\n```python\nimport jmespath\nfrom aws_jmespath_utils import jmespath_options\n\nprint(\n    jmespath.search(\n        \'filter_tags(`["[!Na.]*="]`, @)\',\n        {\n            "a":"b",\n            "Tags": [\n                {"Key": "Name", "Value": "jmespath-utils"},\n                {"Key": "Nam", "Value": "jmespath-utils-nam"},\n                {"Key": "Ebcd", "Value": "edfg"},\n            ]    \n        },\n        options=jmespath_options\n    )\n)\n```\n',
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
