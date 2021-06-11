import pickle

#Pickling a python object
# cars=['BMW','ferrari','audi','jeep','RR']
# file = "mycar.pkl"
# fileobj = open(file,'wb')
# pickle.dump(cars,fileobj)
# fileobj.close()

file="mycar.pkl"
fileobj=open(file,'rb')
mycar=pickle.load(fileobj)
print(mycar)
print(type(mycar))