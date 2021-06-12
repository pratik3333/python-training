try:
    print("I will try this code and will throw exception if there is any problem.")
except Exception as e:
    print("I will run only if try block fails.")
else:
    print("I will run only if there is no exception. Use this to run code which should"
          "only excecute if there is no longer.")
finally:
    print("This will be printed in every case.")