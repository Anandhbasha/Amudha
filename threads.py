import threading
import time

def task1():
    for i in range(5):
        print("Task 1 is running",i)
        time.sleep(1)

def task2():
    for i in range(5):
        print("Task 2 is running",i)
        time.sleep(1)

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

# task1()
# task2()