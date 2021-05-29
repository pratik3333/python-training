from functools import reduce

def sum_num(a,b):
    return (a+b)


li1=reduce(sum_num,[1,3,4,5,6])
print(li1)
    