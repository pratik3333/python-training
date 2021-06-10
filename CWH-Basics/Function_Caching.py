import time
from functools import lru_cache

@lru_cache(maxsize=10)
def some_work(n):
    #some task taking n second
    time.sleep(n)
    return n


if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    print("Now again calling...")
    some_work(3)
    print("again calling...")
    some_work(3)
    print("Done")
