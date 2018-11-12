# yamla
Loading yaml config files as AttributeDict to support `config.easier.readability` .


### Example:
```python
from yamla import load_yaml

config = load_yaml(path)
print(config.strings.hello_world)
```
output:
```python
"Hello World."
```

