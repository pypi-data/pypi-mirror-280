import unittest
from ..cache_loaders import build_and_load_lru_cache


class CacheLoadersTest(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def test_LRU_cache(self):
        cache = build_and_load_lru_cache(max_cache_size=1000)
        self.assertEqual(cache.maxsize, 1000)
        self.assertEqual(cache.currsize, 0)
        cache["key1"] = "value1"
        self.assertEqual(cache.currsize, 1)
        self.assertEqual("key1" in cache, True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
