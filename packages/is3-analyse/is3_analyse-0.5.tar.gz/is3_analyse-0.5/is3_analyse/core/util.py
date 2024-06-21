import numpy as np


class DictToObject:
    def __init__(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                setattr(self, key, DictToObject(value))
            else:
                setattr(self, key, value)


def to_json_serializable(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    elif isinstance(obj, dict):
        return {k: to_json_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple, set)):
        return [to_json_serializable(v) for v in obj]
    elif hasattr(obj, '__dict__'):
        return {k: to_json_serializable(v) for k, v in obj.__dict__().items()}
    else:
        return obj
