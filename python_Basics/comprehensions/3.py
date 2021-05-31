

nums=[1,2,3,4,5,6,7,8,9,10]

#i want 'n' for each 'n' in nums if 'n' is even


my_list=[]
for n in nums:
    if n % 2 ==0:
        my_list.append(n)
print(my_list)

my_list=[n for n in nums if n%2==0]
print(my_list)

#using filter + lambda
my_list=filter(lambda n: n%2==0,nums)
print(my_list)