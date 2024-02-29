import threading
import time

from concurrent.futures import ThreadPoolExecutor

# Indicates some task being done

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)

    return seconds


# time1 = time.perf_counter()

# # func(4)
# # func(3)
# # func(2)

# # time2 = time.perf_counter()
# # print(f"{time2-time1} Seconds Required to Run Normal Function")


# t1=threading.Thread(target=func, args=[4])
# t2=threading.Thread(target=func, args=[3])
# t3=threading.Thread(target=func, args=[2])

# t1.start()
# t2.start()
# t3.start()

# t1.join()  # t1 will stop till execution
# t2.join()  # t2 will stop till execution
# t3.join()  # t3 will stop till execution

# time3 = time.perf_counter()
# print(f"{time3-time1} Seconds Required to Run Multithreding Function")


def poolingDemo():
    with ThreadPoolExecutor() as executor:
        # Method I - ASSIGN SEPERATE PARAMETER

        # feature1 = executor.submit(func, 3)
        # feature2 = executor.submit(func, 2)
        # feature3 = executor.submit(func, 4)
        # print(feature1.result())
        # print(feature2.result())
        # print(feature3.result())

        # Method II - ASSIGN LIST OF PARAMETERS
         l = [1,9,7,10]
         results = executor.map(func, l)
         for result in results:
             print(result)


poolingDemo()


