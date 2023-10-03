### Lists:
___

###  Multi threading vs Multi Processing
#### Process
- separate memory space -> memory not shared between processes
- Heavyweight
- One GIL for each process
- IPC is more complicated
#### Thread
- leightweight
- great for I/O bound tasks
- one thread at a time
- threads share memory
- limited by GIL: one thread at a time
- not interruptable/killable
- careful with race conditions -> change one memory space at the same time
### GIL:
- Global Interpreter Lock
- a lock that allows only on thread at a time to execute in py
- avoid multiprocessing
- reference counting
____
### Threading
- **Daemon thread**: a thread that dies after the main thread dies
- By default, threads are not daemon threads
```python
thread.daemon = True  # demon thread -> background thread that will die when the main thread diethread.daemon = True  # demon thread -> background thread that will die when the main thread die
```
- **Race condition**: two threads accessing the same resource at the same time
- **To deal with race conditions:** lock and release resources or using context managers (`with`)
```python
def increase(lock: Lock):
    global database_value

    lock.acquire()
    local_cp = database_value

    # processing
    local_cp += 1
    
    time.sleep(0.1)
    database_value = local_cp
    lock.release()
# Or with
def increase(lock: Lock):
    global database_value
    
    with lock:
        local_cp = database_value

        # processing
        local_cp += 1
        
        time.sleep(0.1)
        database_value = local_cp

```
**Queues:**
- thread-safe env
- `q.join()`: block main thread until all queue items are done and processed
- `q.task_done()`: marks a thread as done
___
### Multiprocessing:
**Share data between processes**:
- Processes do not share same memory

