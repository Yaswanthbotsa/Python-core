import threading
c = 0
lock = threading.Lock()
def fun():
    global c
    for _ in range(100000):
        with lock:
            c += 1

t1 = threading.Thread(target=fun)
t2 = threading.Thread(target=fun)
t1.start()
t2.start()
t1.join()
t2.join()
print("final c (correct):",c)