list_1=[2,3,4,5,67,443,45,33,5,34,23,75,86,34,756,54,76,45,45]
divide_by_3 = []
for item in list_1:
    if item%3==0:
        divide_by_3.append(item)
print('Without using list comprehensions',divide_by_3)
print("Using List comprehensions",[item for item in list_1 if item%3==0])
        