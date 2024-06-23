from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re

_first_cap_re = re.compile("(.)([A-Z][a-z0-9]+)")
_all_cap_re = re.compile("([a-z0-9])([A-Z])")


def __camelcase_to_snakecase(name):
    s1 = _first_cap_re.sub(r"\1_\2", name)
    return _all_cap_re.sub(r"\1_\2", s1).lower()


def default_name(class_or_fn):
    """Default name for a class or function.

    This is the naming function by default for registries expecting classes or
    functions.

    Args:
      class_or_fn: class or function to be named.

    Returns:
      Default name for registration.
    """
    return __camelcase_to_snakecase(class_or_fn.__name__)


default_object_name = lambda obj: default_name(type(obj))


def display_list_by_prefix(names_list, starting_spaces=0):
    """Creates a help string for names_list grouped by prefix."""
    cur_prefix, result_lines = None, []
    space = " " * starting_spaces
    for name in sorted(names_list):
        split = name.split("_", 1)
        prefix = split[0]
        if cur_prefix != prefix:
            result_lines.append(space + prefix + ":")
            cur_prefix = prefix
        result_lines.append(space + "  * " + name)
    return "\n".join(result_lines)


class Registry(object):
    """
    Dict-like class for managing function/type registrations.
    - a spin-off of the tensor2tensor registry def
    - registry can register function/type against an index as opposed to only a str
    - key defaults using `default_key_fn`

    ```python

    my_registry = Registry("custom_name")

    @my_registry.register
    def my_func():
      pass



    @my_registry.register()
    def another_func():
      pass

    @my_registry.register("non_default_name")
    def third_func(x, y, z):
      pass

    def foo():
      pass

    my_registry.register()(foo)
    my_registry.register("baz")(lambda (x, y): x + y)
    my_register.register("bar")

    print(list(my_registry))
    # ["my_func", "another_func", "non_default_name", "foo", "baz"]
    # (order may vary)

    print(my_registry["non_default_name"] is third_func)  # True
    print("third_func" in my_registry)                    # False
    print("bar" in my_registry)                           # False
    my_registry["non-existent_key"]                       # raises KeyError

    ```
    """

    def __init__(
            self,
            registry_name,
            default_key_fn=default_name,
            validator=None,
            on_set=None,
            value_transformer=(lambda k, v: v),
    ):
        """
          :param registry_name: str identifier for the given registry. Used in error msgs.
          :param default_key_fn (optional): function mapping value -> key for registration
            when a key is not provided
          :param validator (optional): if given, this is run before setting a given (key,
            value) pair. Accepts (key, value) and should raise if there is a
            problem. Overwriting existing keys is not allowed and is checked
            separately. Values are also checked to be callable separately.
          :param on_set (optional): callback function accepting (key, value) pair which is
            run after an item is successfully set.
          :param value_transformer (optional): if run, `__getitem__` will return
            value_transformer(key, registered_value).
        """
        self._registry = {}
        self._name = registry_name
        self._default_key_fn = default_key_fn
        self._validator = validator
        self._on_set = on_set
        self._value_transformer = value_transformer

    @property
    def name(self):
        return self._name

    def register(self, key_or_value=None):
        def decorator(value, key):
            self[key] = value
            return value

        # Handle if decorator was used without parens
        if callable(key_or_value):
            return decorator(value=key_or_value, key=None)
        else:
            return lambda value: decorator(value, key=key_or_value)

    def clear(self):
        self._registry.clear()

    def __setitem__(self, key, value):
        """

        :param key: key to store value under. If `None`, `self.default_key(value)` is used.
        :param value: callable stored under the given key.
        :raises KeyError: if key is already in registry.
        """
        if key is None:
            key = self._default_key_fn(value)

        if key in self:
            raise KeyError(
                "key %s already registered in registry %s" % (key, self._name)
            )

        if not callable(value):
            raise ValueError("value must be callable")

        if self._validator is not None:
            self._validator(key, value)

        if self._on_set is not None:
            key, value = self._on_set(key, value)

        self._registry[key] = value

    def __getitem__(self, key):
        if key not in self:
            raise KeyError(
                "%s never registered with registry %s. Available:\n %s"
                % (str(key), self.name, display_list_by_prefix(sorted(self), 4))
            )
        value = self._registry[key]
        return self._value_transformer(key, value)

    def __contains__(self, key):
        return key in self._registry

    def __iter__(self):
        return iter(self._registry)

    def __len__(self):
        return len(self._registry)


class Registries(object):
    """Object holding `Registry` objects."""

    def __init__(self):
        raise RuntimeError("Registries is not intended to be instantiated")

    indexes = Registry("indexes")
    models = Registry("models")
    protocols = Registry("protocols")


# Need to import classes in __init__.py for which respective registry annotations are used, in order to register them.

list_indexes = lambda: sorted(Registries.indexes)
register_index = Registries.indexes.register

list_protocols = lambda: sorted(Registries.protocols)
register_protocol = Registries.protocols.register

list_models = lambda: sorted(Registries.models)
register_model = Registries.models.register


def get_index(index_type):
    return Registries.indexes[index_type]


def model(model_type):
    """
    :param model_type: string model_type
    """
    return Registries.models[model_type]


def get_protocol(protocol_name, **inputs):
    """
    :param protocol_name: string protocol_name
    """
    return Registries.protocols[protocol_name](**inputs)


class Index:
    pass


def help_string():
    """Generate help string with contents of registry."""
    help_str = """
Registry contents:
------------------

 indexes:
%s

 protocols:
%s
"""
    lists = tuple(
        display_list_by_prefix(entries, starting_spaces=4)
        for entries in [  # pylint: disable=g-complex-comprehension
            list_indexes(),
            list_protocols()
        ]
    )
    return help_str % lists
