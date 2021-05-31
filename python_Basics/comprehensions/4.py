

nums=[1,2,3,4,5,6,7,8,9,10]

#I want (letters,nums) pair for each letter in 'abcd' and each number in '0123'
# my_list=[]
# for letter in 'abcd':
#     for nums in range(4):
#         my_list.append((nums,letter))
#
# print(my_list)

my_list=[(nums,letters) for letters in 'abcd' for nums in range(4) ]
print(my_list)