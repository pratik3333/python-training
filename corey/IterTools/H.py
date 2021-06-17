import itertools

letters=['a','b','c','d']
number=[0,1,2,3]
name=['jack','john']

combined=itertools.chain(letters,number,name)

for item in combined:
    print(item)