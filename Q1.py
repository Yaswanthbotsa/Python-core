# 1. Write a Python program that creates a worker thread which prints “Hello
# from worker thread” while the main thread prints “Hello from main thread”, and
# ensure that the main thread waits for the worker thread to finish execution
# before the program exits.

import threading
import time


def worker():
    print("This is HELLO from worker thread")
    time.sleep(0.9)

t1 = threading.Thread(target=worker)
t1.start()
t1.join()
print("Hello from main thread")