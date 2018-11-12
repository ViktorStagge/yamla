# yamla
Loading yaml config files as AttributeDict to support `config.easier.readability` .


### Example:
```python
>>> config = load_yaml(path)
>>> print(config.strings.hello_world)
"Hello World."
```
