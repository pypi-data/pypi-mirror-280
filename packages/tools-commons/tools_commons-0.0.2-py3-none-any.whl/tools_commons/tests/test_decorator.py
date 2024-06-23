import unittest
from time import perf_counter

from ..decorator import retry, timeit


class DecoratorTest(unittest.TestCase):
    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()
    
    def test_retry(self):
        control_func = lambda x: x[0]
        decorator = retry(TypeError, delay=2)
        retry_func = decorator(control_func)
        start = perf_counter()
        with self.assertRaises(TypeError, msg="'int' object is not subscriptable"):
            retry_func(3)
        end = perf_counter()
        self.assertAlmostEqual(end-start, 14, places=1)
    
    def test_timeit(self):        
        def control_func(x, *args, **kw):
            return x
        timed_func = timeit(control_func)
        log_time = {}
        result = timed_func('identity', log_time=log_time)
        self.assertEqual(result, 'identity')
        self.assertEqual(log_time['CONTROL_FUNC'], 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)