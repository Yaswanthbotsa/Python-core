# 10. Write a Python program using ThreadPoolExecutor with three worker threads
# that submits tasks to compute the square of numbers from 1 to 5 and prints each
# result as soon as the corresponding task completes.

from concurrent.futures import ThreadPoolExecutor

def fun(x):
    print("Inside function")
    return x+1
l = [1,2,3,4,5]
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(fun,i) for i in l]
    futures2 = executor.map(fun,l)
    for i in futures2:
        print(i)