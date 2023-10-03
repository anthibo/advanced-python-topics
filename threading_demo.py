from threading import Thread, Lock, current_thread
from queue import Queue
import os
import time

database_value = 0


def increase(lock: Lock):
    global database_value

    # lock resources with context managers
    with lock:
        local_cp = database_value

        # processing
        local_cp += 1

        time.sleep(0.1)
        database_value = local_cp


def worker(q: Queue, lock: Lock):
    while True:
        value = q.get()

        # processing
        with lock:
            print(f"in {current_thread().name} got {value}")
        q.task_done()  # marks a thread as done


if __name__ == "__main__":
    # lock = Lock()
    # print("start value", database_value)
    # thread1 = Thread(target=increase, args=(lock,))
    # thread2 = Thread(target=increase, args=(lock,))
    # thread1.start()
    # thread2.start()
    # thread1.join()
    # thread2.join()
    # print("env val", database_value)

    q = Queue()
    lock = Lock()

    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock,))
        thread.daemon = True  # demon thread -> background thread that will die when the main thread die
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()  # block main thread until all queue items are done and processed

    print("end main")
