import pickle

from overrides import overrides

from .protocol import Protocol
from ..registry import register_protocol


@register_protocol("pickle")
class MyPickle(Protocol):

    def __init__(self):
        super().__init__()

    @overrides
    def serialize(self, object_val, path: str) -> None:
        with open(path, 'wb') as output:
            try:
                pickle.dump(object_val, output)
            finally:
                output.close()

    @overrides
    def deserialize(self, path: str) -> None:
        with open(path, "rb") as f:
            try:
                return pickle.load(f)
            finally:
                f.close()