# import threading
# import time
#
# def square(num):
#     print(f"Square: {num*num}")
#     time.sleep(9)
#
# def cube(num):
#     print(f"Cube: {num*num*num}")
#     time.sleep(1)
#
# t1 = threading.Thread(target=square, args=(2,))
# t2 = threading.Thread(target=cube, args=(4,))
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()
#
# print("Done!")
import time
from concurrent.futures import ThreadPoolExecutor

def worker(task):
    print(f"Task {task} running")

# Create a thread pool with 2 workers
with ThreadPoolExecutor(max_workers=2) as executor:
    # Submit two tasks to run in parallel
    executor.submit(worker, 1)
    executor.submit(worker, 2)
    time.sleep(2)
    executor.submit(worker, 3)

# from concurrent.futures import ThreadPoolExecutor
# import time
#
# def worker(task):
#     print(f"Task {task} STARTED")
#     time.sleep(2)                    # simulate slow task
#     print(f"Task {task} FINISHED")
#
# with ThreadPoolExecutor(max_workers=2) as executor:
#     executor.submit(worker, 1)
#     executor.submit(worker, 2)
#     executor.submit(worker, 3)

