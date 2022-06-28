with open('Robin.txt', 'r') as f:
    last_line = f.readlines()[-5:]
print(last_line)