users=['pratik','kunal','nik','jay','viru']
mobiles=['Apple','MI','VIVO','Nokia','Samsung']

for i in range(0,len(users)):
    template="Mobile used by {} is {}" #{0} {1}
    print(template.format(users[i],mobiles[i]))