class Library:
    def __init__(self,list,name):
        self.bookList=list
        self.name=name
        self.lendDict={}

    def displayBook(self):
        print(f"we have following books in our library: {self.name}")
        for book in self.bookList:
            print(book)

    def lendBook(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender-Book database has been updated.you can take the book now")
        else:
            print(f"Book alredy being used bye {self.lendDict[book]}")

    def addBook(self,book):
        self.bookList.append(book)
        print("Book has been added to the book list")

    def returnBook(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    pratik=Library(['The monk who sold his Ferrari','Why not me?','One life to Ride',
                    'A few thousand kilometers of Happiness'],"Codewithpratik")

    while(True):
        print(f"welcome to the {pratik.name} library. Enter your choice to continue")
        print("1. Display the book")
        print("2. Lend a the book")
        print("3. Add  a book")
        print("4. Return a book")
        user_choice=input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue
        else:
            user_choice=int(user_choice)

        if user_choice == 1:
            pratik.displayBook()

        elif user_choice == 2:
            book=input("Enter the name of the book you want to lend:")
            user=input("Enter your name:")
            pratik.lendBook(user,book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to Add:")
            pratik.addBook(book)

        elif user_choice ==4:
            book = input("Enter the name of the book you want to Return:")
            pratik.returnBook(book)

        else:
            print("Not a valid option")

        print("press q to quit and c to continue")
        user_choice2=""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q".lower():
                exit()
            elif user_choice2 == "c".lower():
                continue


