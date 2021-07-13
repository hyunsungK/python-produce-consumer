from multiprocessing import Process, Queue, cpu_count
import random
import time


def serve(queue):
    works = ["task_1", "task_2"]
    while True:
        time.sleep(1)
        queue.put(random.choice(works))
