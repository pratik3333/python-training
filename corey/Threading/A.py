import time
import threading

start=time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds}second(s)...')
    time.sleep(seconds)
    print('Done sleeping...')

threds=[]

for _ in range(100):
    t=threading.Thread(target=do_something,args=[1.5])
    t.start()
    threds.append(t)

for thred in threds:
    thred.join()



finish=time.perf_counter()

print(f'finish in{round(finish-start,2)} second(s)')