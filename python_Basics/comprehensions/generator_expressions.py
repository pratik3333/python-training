

#generator expression
#I want to yield 'n*n' for each 'n' in nums

nums=[1,2,3,4,5,6,7,8,9,10]

#def my_func(nums):
  #  for n in nums:
 #       yield n*n

#my_gen=my_func(nums)

my_gen=(n*n for n in nums)
for i in my_gen:
    print(i)