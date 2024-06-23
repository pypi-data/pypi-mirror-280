import unittest
import asyncio
from ..misc_utils import *


class Test(unittest.TestCase):
    def setUp(self):
        self._val = 0
        self._exeptions = 0
        super().setUp()

    def tearDown(self):
        super().tearDown()
        close_loop()

    async def A(self):
        self._val += 1
        raise RuntimeError("My error")

    def B(self):
        try:
            run_co_routine(self.A())
        except Exception:
            self._exeptions += 1

        try:
            run_co_routine(self.A())
        except Exception:
            self._exeptions += 1

    async def C(self):
        self.B()

    def test_runcoroutinr(self):
        asyncio.get_event_loop().run_until_complete(self.C())
        print(self._exeptions)
        print(self._val)
        assert self._exeptions == 2
        assert self._val == 2


    async def _test_wait_for_1(self):
        await wait_for(asyncio.sleep(5), timeout=1)

    async def _test_wait_for_2(self):
        await wait_for(asyncio.sleep(1), timeout=2)

    def test_wait_for(self):
        with self.assertRaises(asyncio.TimeoutError):
            asyncio.get_event_loop().run_until_complete(self._test_wait_for_1())
        asyncio.get_event_loop().run_until_complete(self._test_wait_for_2())


if __name__ == "__main__":
    unittest.main(verbosity=2)
