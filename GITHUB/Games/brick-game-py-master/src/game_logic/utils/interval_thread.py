import threading
import time


class Interval(threading.Thread):
    def __init__(self, interval, callback, name=''):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.callback = callback
        self.interval = interval
        self._is_terminated = False
        self.name = name
    
    def terminate(self):
        self._is_terminated = True
    
    def run(self):
        while not self._is_terminated:
            time.sleep(self.interval)
            self.callback()
