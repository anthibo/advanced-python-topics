from multiprocessing import Process
import os
import time

from threading import Thread

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)


# MultiProcessing
processes: list[Process] = []
num_processes = os.cpu_count()

# create processes
for i in range(num_processes):
    p = Process(target= square_numbers)
    processes.append(p)

# start
for p in processes:
    p.start()

# join
for p in processes:
    p.join()

# Multithreading
threads: list[Thread] = []
num_threads = 10

# create processes
for i in range(num_threads):
    t = Thread(target= square_numbers)
    threads.append(t)

# start
for t in threads:
    t.start()

# join
for t in threads:
    t.join()
    
print('end main thread')