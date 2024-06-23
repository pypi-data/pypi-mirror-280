import unittest
from ..collections import LoadingDict


class LoadingDictTest(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_signature(self):
        dic = LoadingDict(lambda x: -x)
        self.assertEqual(-1, dic[1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
