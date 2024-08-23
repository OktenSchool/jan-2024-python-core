import threading
import time


# print('ddd')
# print(threading.current_thread().name)

# def show(n):
#     for i in range(n):
#         print(i, threading.current_thread().name)
#         time.sleep(0.5)
# thread1 = threading.Thread(target=show, args=(5, ))
# thread2 = threading.Thread(target=show, args=(10, ))
# thread1.start()
# thread1.join()
# thread2.start()
# thread2.join()
# show(15)

count = 0
lock = threading.Lock()


def inc():
    with lock:
        global count
        count += 1
        print(count)

threads = []


for _ in range(1000):
    thread = threading.Thread(target=inc)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()