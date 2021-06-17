import itertools

number=[0,1,2,3]

result=itertools.product(number,repeat=4)


for item in result:
    print(item)