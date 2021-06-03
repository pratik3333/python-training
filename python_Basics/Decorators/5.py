


def arg_func(normal,*args,**kwargs):
    print(normal)
    for item in args:
        print(item)

    print("\nNow i would like to introduce some of our heros")
    for key, value in kwargs.items():
        print(f'{key} is the {value}')

har=['Kunal','Harry','Pratik']

normal="I am the normal argument and students are"

kw={'Kunal':'Moniter','Harry':'Gym instructer'}

arg_func(normal,*har,**kw)