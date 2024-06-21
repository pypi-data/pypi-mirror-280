import inspect
from abc import abstractmethod


def get_param_names(func):
    signature = inspect.signature(func)
    return [param.name for param in signature.parameters.values()
            if param.kind == param.POSITIONAL_OR_KEYWORD]


class BaseAlgorithm:
    def __init__(self) -> None:
        self.param_names = get_param_names(self.implement)

    @staticmethod
    def add_subclass(algorithm):
        BaseAlgorithm.__subclasses__().append(algorithm)

    @abstractmethod
    def implement(self, *args, **kwargs):
        pass
