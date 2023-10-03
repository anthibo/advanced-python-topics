from multiprocessing import Process, Value, Array, Lock, Queue, Pool
import os
import time


def add_100(numbers: Array, lock: Lock):
    for x in range(100):
        time.sleep(0.1)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1

def square(numbers: list[int], queue: Queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers: list[int], queue: Queue):
    for i in numbers:
        queue.put(-1 * i)

def cube(n: int):
    return n * n * n

if __name__ == "__main__":
    lock = Lock()
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print("Number at the beginning is", shared_array[:])

    p1  = Process(target=add_100, args=(shared_array,lock))
    p2  = Process(target=add_100, args=(shared_array,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Number at the end is", shared_array[:])

    # ========= Queue Example ============
    numbers = range(1, 6)
    q = Queue()

    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=make_negative, args=(numbers, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())

    # ========= Pool Example ============
    numbers = range(10)
    pool = Pool()
    
    # map, apply, join, close
    results = pool.map(cube, numbers) # allocates processes based on CPU cores
    result = pool.apply(cube, (numbers[3],)) # executes for one argument

    pool.close() # must run before pool.join()
    pool.join() # awaits for results

    print(results)
    print(result)
