# 4. Write a Python program where two threads increment a shared variable named
# counter exactly 100000 times each without using any synchronization mechanism,
# and print the final value of the counter to demonstrate inconsistent or
# incorrect results caused by a race condition.

import threading
c = 0
def fun():
    global c
    for _ in range(100000):
        c += 1

t1 = threading.Thread(target=fun)
t2 = threading.Thread(target=fun)
t1.start()
t2.start()
t1.join()
t2.join()
print("final c (incorrect due to race condition):",c)

print("-------------")
