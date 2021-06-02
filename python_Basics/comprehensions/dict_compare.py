

nums=[1,2,3,4,5,6,7,8,9,10]

#dictionary comprehensions

names=['bruce','clark','peter','kunal','digvijay']
heros=['Batman','superman','makrand','salman','vidyut']

#I want a dict{'name':hero} for each name, hero in zip(name,heros)

my_dict={name:hero for name, hero in zip(names,heros) if name != 'bruce'}
print(my_dict)
