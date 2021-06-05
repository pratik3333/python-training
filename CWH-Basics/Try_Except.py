

num1=input("Enter the first number: ")
num2=input("Enter the second number: ")

try:
    print("The Sum of this two numbers ",
          int(num1)+int(num2),'\n')
except  Exception as e:
    print(e)

print("Bye")