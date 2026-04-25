# 9. Write a Python program that starts a daemon thread running an infinite
# loop which repeatedly prints “Running in background”, while the main thread
# sleeps for two seconds and then exits, and observe what happens to the daemon
# thread when the main program terminates.

import threading

def fun():
    while True:
        print("Infinite Loop Running")

t1 = threading.Thread(target=fun,name = "Thread-1",daemon=True)
t2 = threading.Thread(target=fun,name = "Thread-2",daemon=True)

t1.start()
t2.start()
print("Main-Thread")
