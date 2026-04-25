# 6. Write a Python program where one thread prints “A started” and then sleeps
# for two seconds, another thread prints “B started”, and the execution order is
# controlled in such a way that the second thread starts only after the first
# thread has completely finished.

import threading
import time
def fun():
    print("A thread started")
    time.sleep(2)
def fun1():
    print("B thread started")
t1 = threading.Thread(target=fun)
t2 = threading.Thread(target=fun1)
t1.start()
t1.join()
t2.start()
t2.join()
print("Main Thread")