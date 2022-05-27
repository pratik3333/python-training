
de={'one':'abc','two':'atc','three':'ytr','four':'cndj'}

w=input("Enter a number for searching: ")



for i,j in de.items():
    if i==w:
        print(j)
    else:
        continue

