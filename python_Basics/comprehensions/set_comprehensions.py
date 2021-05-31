

#set comprehension
nums=[1,1,2,3,3,4,5,4,5,6,7,7,8,8,9,9]
# my_set=set()
# for n in nums:
#     my_set.add(n)
# print(my_set)

my_set={n for n in nums}
print(my_set)