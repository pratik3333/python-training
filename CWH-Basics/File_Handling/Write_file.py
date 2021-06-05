

# f=open('Robin.txt','a')
# #f=open('Robin.txt','w')
# f.write("\nMost people live-Whether physically,intellectually\nor morally-in avery restricted circle of their potential\nbeing. We all have reaservoirs of life to draw upon of \nwhich we do not dream.         \n\nWilliam James\n")
# f.close()

# #Handle read and write both
f=open("Robin.txt","r+")
print(f.read())
f.write("Thank you")