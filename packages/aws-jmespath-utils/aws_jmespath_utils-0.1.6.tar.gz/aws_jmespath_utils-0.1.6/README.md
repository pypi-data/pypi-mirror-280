# aws-jmespath-utils

## Installation

```bash
pip3 install aws_jmespath_utils
```

## Usage

```python
import jmespath
from aws_jmespath_utils import jmespath_options

print(
    jmespath.search(
        'filter_tags(`["[!Na.]*="]`, @)',
        {
            "a":"b",
            "Tags": [
                {"Key": "Name", "Value": "jmespath-utils"},
                {"Key": "Nam", "Value": "jmespath-utils-nam"},
                {"Key": "Ebcd", "Value": "edfg"},
            ]    
        },
        options=jmespath_options
    )
)
```
