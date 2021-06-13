import bisect

number=5

list1=[1,2,3,4,6,7,8,9]
print(bisect.bisect(list1,number))
bisect.insort(list1,number)
print(list1)