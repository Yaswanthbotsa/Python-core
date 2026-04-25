# 7. Write a Python program in which three worker threads wait until a
# synchronization signal is received, the main thread sleeps for two seconds and
# then signals all waiting threads using an event, after which each worker thread
# prints a message indicating that it has started execution.

import threading
import time

e = threading.Event()
def fun():
    print(f"Thread name: {threading.current_thread().name} is started")
    e.wait()
    print(f"Thread name: {threading.current_thread().name} is stopped")

t1 = threading.Thread(target=fun,name="Thread-1")
t2 = threading.Thread(target=fun,name="Thread-2")
t3 = threading.Thread(target=fun,name="Thread-3")
t1.start()
t2.start()
t3.start()

time.sleep(2)
e.set()
print("Main Thread done")