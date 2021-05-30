

def outer():
    x='outer X'

    def inner():
        nonlocal x
        x='inner x'
        print(x)

    inner()
    #print(x)

#outer()