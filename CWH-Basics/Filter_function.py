list_1=[2,3,4,5,6,7,8,9,10]

def greater_5(num):
    return num>5

greater_tha_5=list(filter(greater_5,list_1))
print(greater_tha_5)