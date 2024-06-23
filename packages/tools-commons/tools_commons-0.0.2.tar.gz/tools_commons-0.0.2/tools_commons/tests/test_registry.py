import unittest

from ..registry import *


class JustALongClassName:
    pass


class RegistryTest(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_default_name(self):
        default_class_name = default_name(JustALongClassName)
        self.assertEqual(default_class_name, "just_a_long_class_name")

    def test_list_display(self):
        list_of_names = ["message_batch", "message_processor",
                         "pre_processing", "pre_processing_batch",
                         "intent_answers", "intent_questions", "intent_processing"]
        prefix_list_string = display_list_by_prefix(list_of_names)
        expected_string = "intent:\n  * intent_answers\n  * intent_processing\n  * intent_questions\n" + \
                          "message:\n  * message_batch\n  * message_processor\n" + \
                          "pre:\n  * pre_processing\n  * pre_processing_batch"
        self.assertEqual(prefix_list_string, expected_string)

    def test_registry(self):
        # Testing registry name
        registry = Registry('sample_registry')
        self.assertEqual(registry.name, 'sample_registry')

        # Testing registry __setitem__ and __getitem__ methods
        control_func = lambda x: x
        registry['identity'] = control_func
        self.assertEqual(registry['identity'], control_func)
        with self.assertRaises(KeyError, msg='key identity already registered in registry sample_registry'):
            registry['identity'] = control_func
        with self.assertRaises(KeyError, msg='something_else never registered with registry sample_registry.'
                                             ' Available:\n     identity:\n      * identity'):
            registry['something_else']

        # Testing registry __contains__ method
        self.assertTrue('identity' in registry)

    def test_registries(self):
        def control_func(x):
            return (lambda v: v)(x)

        register_index(control_func)
        self.assertEqual(get_index('control_func'), control_func)

        with self.assertRaises(KeyError, msg='something_else never registered with registry indexes.'
                                             ' Available:\n     control:\n      * control_func'):
            get_index('something_else')

        self.assertEqual(help_string(), "\nRegistry contents:\n------------------\n\n indexes:"
                                        "\n    control:\n      * control_func\n\n protocols:\n\n")

    def test_basic(self):
        r = Registry("test_registry")
        r["hello"] = lambda: "world"
        r["a"] = lambda: "b"
        self.assertEqual(r["hello"](), "world")
        self.assertEqual(r["a"](), "b")

    def test_default_key_fn(self):
        r = Registry("test", default_key_fn=lambda x: x().upper())
        r.register()(lambda: "hello")
        self.assertEqual(r["HELLO"](), "hello")

    def test_value_transformer(self):
        r = Registry(
            "test_registry",
            value_transformer=lambda x, y: x + y()
        )
        r.register(3)(lambda: 5)
        self.assertEqual(r[3], 8)


if __name__ == "__main__":
    unittest.main(verbosity=2)
