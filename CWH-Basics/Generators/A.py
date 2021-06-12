"""
Iterables
Iterator
Iteration
"""

def gen(n):
    for i in range (n):
        yield i


#print(gen(100000000))
#
# for i in gen(1000):
#     print(i)
#
# obj1=gen(100)
# print(next(obj1))
# print(next(obj1))
# print(next(obj1))


obj1=gen(3)
print(next(obj1))
print(next(obj1))
print(next(obj1))
print(next(obj1))
