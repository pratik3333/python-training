# a=input("What is your name:")
# b=input("HOw much do you earn:")
# if int(b)==0:
#     raise ZeroDivisionError("b is 0 so stopping the program")
# if a.isnumeric():
#     raise Exception("Number are not allowed")
#
# print(f"Hello {a}")

c=input("Enter your name:").lower()
try:
    print(a)

except Exception as e:
    if c=="pratik":
        raise ValueError("Pratik is blocked he is not allowed")
    print("Exception handled")
