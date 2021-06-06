

f=open("Robin.txt")

print(f.readline())
#print(f.tell()) #Where is your pointer
f.seek(11)
print(f.readline())
#print(f.tell())
f.close()