import threading

class Counter:

    def __init__(self, start: int = 0) -> None:
        self.counter = start
        self.lock = threading.Lock()

    def __next__(self) -> int:
        with self.lock:
            i = self.counter
            self.counter += 1
        return i

    def reset(self) -> None:
        with self.lock:
            self.counter = 0
