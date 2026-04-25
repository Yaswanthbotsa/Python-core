# 8. Write a Python program that creates five threads competing for a shared
# resource, restricts access so that only two threads can enter the critical
# section at the same time using a semaphore, and prints a message whenever a
# thread enters and exits the critical section.

import threading
import time
s = threading.Semaphore(2)
x = 0

def fun():
    global x
    with s:
        x += 1
        print(x)
        print(f"{threading.current_thread().name} thread done")
t1 = threading.Thread(target=fun)
t2 = threading.Thread(target=fun)
t3 = threading.Thread(target=fun)
t4 = threading.Thread(target=fun)
t5 = threading.Thread(target=fun)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()





