import time
import concurrent.futures

start=time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return 'Done sleeping...'

with concurrent.futures.ThreadPoolExecutor() as executer:
    result=[executer.submit(do_something,1) for _ in range(10)]


    for f in concurrent.futures.as_completed(result):
        print(f.result())


# threads=[]
#
# for _ in range(10):
#     t=threading.Thread(target=do_something,args=[1.5])
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()



finish=time.perf_counter()

print(f'finish in {round(finish-start,2)} second(s)')