
#
# ls=[i for i in range(100) if i%3==0]
# print(ls)
#
# la=[i for i in range(0,1000,5)]
# print(la)

#
# dict1={i:f"item{i}"for i in range(10)}
#
# dict2={value:key for key, value in dict1.items()}
# print(dict1,'\n',dict2)

evens={i for i in range(100) if i%2==0}
for item in evens:
    print(item)