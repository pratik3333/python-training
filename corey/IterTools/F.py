import itertools

letters=['a','b','c','d']
numbers=[0,1,2,3]
names=['jack','john']

result=itertools.combinations(letters,2)

for item in result:
    print(item)