

n=18
number_of_guesses=1
print("Nummber of guesses is limited to only 9 times: ")
while (number_of_guesses<=9):
    guesses_number = int(input("Guess the number: \n"))
    if guesses_number<18:
        print("You enter less number please input greater number.\n")
    elif guesses_number>18:
        print("You enter greater number please input smaller number.\n")
    else:
        print("you Won\n")
        print(number_of_guesses,"no.of guesses he took to finish")
        break
    print(9-number_of_guesses,"no.of guesses left")
    number_of_guesses = number_of_guesses + 1

if (number_of_guesses>9):
    print("Game over")