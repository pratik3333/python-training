import itertools

counter=itertools.repeat(5, times=10)

# square=map(pow,range(100),itertools.repeat(2))
# print(list(square))

square2=itertools.starmap(pow,[(0,2),(1,2),(2,2),(3,2),(4,2)])
print(list(square2))


#
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))