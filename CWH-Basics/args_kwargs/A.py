#*args and **kwargs

def function_1(*args):
    print(type(args))
    if (len(args)==3):
        print("The name of the student is",args[0],"and age is",args[1],"and rollno is",args[2])
    else:
        print("The name of the student is",args[0],"and age is",args[1])


#function_1('pratik',21,34)
#
# lis1=['pratik',21,345]
# function_1(*lis1)

def printmarks(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,value)

def master(normal,*args,**kwargs):
    print(normal)
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(key,value)

lis=['harry',21,567]

marklist={'pratik':100,'kunal':99,'nikhil':89,'aditya':76,'digvijay':44}

#printmarks(**marklist)
master("normal args",*lis,**marklist)