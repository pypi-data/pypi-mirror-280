# aws-jmespath-utils

## Installation

```bash
pip3 install aws_jmespath_utils
```

## Usage

```python
jmespath.search(  # it's important that your expression array must be inside `` backticks
    '[] | filter_tags(`["Name=*"]`, @)', data_list, options=jmespath_options
)
```

```python
jmespath.search(  # it's important that your expression array must be inside `` backticks
    '[] | filter_tags(`["[!Name]="]`, @)', data_list, options=jmespath_options
)

```


```bash
# set log level as you wish
export AWS_JMESPATH_UTILS_LOG_LEVEL="DEBUG"   
export AWS_JMESPATH_UTILS_LOG_LEVEL="WARNING"   
export AWS_JMESPATH_UTILS_LOG_LEVEL="INFO"  # default   
```

