def greater_than_2(n):
    if n>2:
        return True
    else:
        return False

h1=[1,2,3,4,5,6,7,8,9,0,4]

greater_th_2=list(filter(greater_than_2,h1))

print(greater_th_2)