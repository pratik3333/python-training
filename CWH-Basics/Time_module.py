

import time

initial=time.time()
print(initial)

k=0
while (k<45):
    time.sleep(0.5)
    print("Pratik")
    k +=1
print("While loop in ran",time.time()-initial,"seconds")

localtime=time.asctime(time.localtime(time.time()))
print(localtime)

