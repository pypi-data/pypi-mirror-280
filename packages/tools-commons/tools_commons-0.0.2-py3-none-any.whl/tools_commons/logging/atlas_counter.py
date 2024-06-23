import datetime
import logging
import os
import time
from collections import defaultdict
from collections import deque
from logging.handlers import RotatingFileHandler
from multiprocessing import Lock
from threading import Thread, Event

import schedule as schedule

from ..singleton import Singleton

window = 6
rolling_period = 30
logging_period = 60

logger = logging.getLogger("ATLAS_COUNTER")
logger.setLevel(logging.DEBUG)
LOGFILE = "/tmp/logs/atlas-counters.log"
os.makedirs(os.path.dirname(LOGFILE), exist_ok=True)
handler = RotatingFileHandler(LOGFILE, maxBytes=(1048576 * 5), backupCount=7, mode="w")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


class AtlasCounter(Singleton):
    def __init__(self):
        super(AtlasCounter, self).__init__()
        self.__counter = defaultdict(int)
        self.__window_counter = defaultdict(int)
        self.__rolling_window = defaultdict()
        self._lock = Lock()

    def inc(self, counter_name, n=1):
        with self._lock:
            self.__counter[counter_name] += n
            self.__window_counter[counter_name] += n

    @staticmethod
    def default_queue(max_len=6):
        return deque([0] * max_len, maxlen=max_len)

    def value(self, counter_name):
        with self._lock:
            return self.__counter.get(counter_name, 0)

    def counters(self):
        with self._lock:
            return self.__counter

    def counter_names(self):
        with self._lock:
            return self.__counter.keys()

    def __reset_window(self):
        win_count = self.__window_counter
        self.__window_counter.clear()
        return win_count

    def roll_window(self):
        with self._lock:
            for counter_key in self.__counter.keys():
                counter_value = self.__window_counter[counter_key]
                queue = self.__rolling_window.get(counter_key, self.default_queue())
                queue.append(counter_value)
                self.__rolling_window[counter_key] = queue
            self.__window_counter = defaultdict(int)
            return self.__rolling_window, self.__counter

    def get_window(self):
        with self._lock:
            return self.__rolling_window


class AtlasLogger(Singleton):
    def __init__(self):
        self.logger_thread_stop = Event()
        logger_thread = Thread(
            target=self.logger, args=(atlas_counter, self.logger_thread_stop), daemon=True
        )
        logger_thread.start()
        self.time = time.time()

    def logger(self, counter, stop_event):
        # schedule.every(rolling_period).seconds.do(self.update_window, counter)
        schedule.every(logging_period).seconds.do(self.log_counters, counter)
        while not stop_event.is_set():
            schedule.run_pending()
            time.sleep(10)

    def log_counters(self, counter):
        uptime = time.time() - self.time
        logger.info(
            "\n------------------------Uptime - %s------------------------------\n",
            str(datetime.timedelta(seconds=uptime)),
        )
        rolling_window, counters = counter.roll_window()
        with counter._lock:
            for counter_key, counter_value in counters.items():
                seq = (
                    "["
                    + "%-12i%-12i%-12i%-12i%-12i%-12i"
                    % tuple(rolling_window.get(counter_key))
                    + "]",
                    str(counter_value),
                    str(counter_key),
                )
                logger.info("\t".join(seq))

    def stop(self):
        self.logger_thread_stop.set()


atlas_counter = AtlasCounter()
atlas_logger = AtlasLogger()
