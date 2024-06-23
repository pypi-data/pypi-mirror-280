import unittest
from ..exceptions import *


class ExceptionsTest(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_request_timeout_exception(self):
        try:
            raise RequestTimeoutError("your request is taking too much time, getting timeouts")
        except Exception as e:
            self.assertEqual(type(e), RequestTimeoutError)
            self.assertEqual(str(e), "your request is taking too much time, getting timeouts")


if __name__ == "__main__":
    unittest.main(verbosity=2)
