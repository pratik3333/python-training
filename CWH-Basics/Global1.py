
l=10 #Global


def function(n):
    #l=5 #Local
    m=6
    global l
    l=l+45
    print(l, m)
    print(n,"I have printed")
function("This is me")