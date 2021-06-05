


#
# i=0
#
# while(True):
#     print(i)
#     if (i==10):
#         break
#     i +=1

while(True):
    inp=int(input("Enter the value: "))
    if inp>100:
        print("Congrats you have entered a number greater than 100")
        break
    else:
        print("Try again!",'\n')
        continue