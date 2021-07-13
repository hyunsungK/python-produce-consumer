from multiprocessing import Process, Queue, cpu_count
import random
import time

from producer import serve
from consumer import work


class Manager:
    def __init__(self):
        self.queue = Queue()
        self.NUMBER_OF_PROCESSES = cpu_count()

    def start(self):
        print(f"starting {self.NUMBER_OF_PROCESSES} workers")
        self.workers = [Process(target=work, args=(i, self.queue,)) for i in range(self.NUMBER_OF_PROCESSES)]
        for w in self.workers:
            w.start()

        serve(self.queue)

    def stop(self):
        self.queue.put(None)
        for i in range(self.NUMBER_OF_PROCESSES):
            self.workers[i].join()
        self.queue.close()


if __name__ == "__main__":
    Manager().start()
