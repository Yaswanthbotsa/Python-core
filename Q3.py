# 3. Write a Python program in which a thread accepts two integer arguments,
# computes their sum, prints the result from inside the thread, and ensures that
# the main thread waits until the worker thread completes execution

import threading
import time


def fun(x,y):
    start = time.time()
    z = x + y
    print(z)
    print("%.2fs" %(time.time()-start))
    print(f"{time.time() - start :.2f}")

t2 = threading.Thread(target=fun,args=(2,3))
t1 = threading.Thread(target=fun,args=(1,2))
t1.start()
t2.start()
t1.join()
t2.join()

print("Ended Main Thread")