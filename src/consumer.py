import time


def work(id, queue):
    while True:
        task = queue.get()
        if task is None:
            break
        time.sleep(0.05)
        print(f"{id}, {task}")
    queue.put(None)
