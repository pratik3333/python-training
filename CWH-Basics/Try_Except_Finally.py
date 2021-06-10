try:
    f=open('pratik.txt')
   #f=open('harry-ex.txt')

except Exception as e:
    print(e)
else:
    print("This will run only if except is not running")
finally:
    print("Run this anyway....")
    try:
        f.close()
    except Exception as e:
        print(e)
