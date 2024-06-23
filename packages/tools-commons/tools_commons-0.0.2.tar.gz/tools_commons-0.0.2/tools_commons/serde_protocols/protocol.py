from abc import ABCMeta, abstractmethod


class Protocol(metaclass=ABCMeta):

    def __init__(self):
        pass

    @abstractmethod
    def serialize(self, object, path: str) -> None:
        pass

    @abstractmethod
    def deserialize(self, path: str) -> None:
        pass
