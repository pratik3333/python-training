#printing patterns

for i in range(0,5):
    for j in range(0,i+1):
        if (j%2==0):
            print("*",end=" ")
        else:
            print("#",end=" ")
    print()



