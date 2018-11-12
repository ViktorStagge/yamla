import yaml


def key_value_generator(it):
    if isinstance(it, dict):
        it = it.items()

    for key, value in it:
        if isinstance(value, dict):
            yield (key, AttributeDict(value))
        else:
            yield (key, value)


class AttributeDict(dict):
    def __init__(self, iterable, **kwargs):
        kv = key_value_generator(iterable)
        super().__init__(kv, **kwargs)

    def __getitem__(self, key):
        return super().__getitem__(key)

    def __getattr__(self, key):
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        if isinstance(value, dict):
            value = AttributeDict(value)
        super().__setitem__(key, value)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __delattr__(self, key):
        super().pop(key)


def load_yaml(path):
    with open(path) as file:
        config = yaml.load(file)
    config = AttributeDict(config)
    return config
