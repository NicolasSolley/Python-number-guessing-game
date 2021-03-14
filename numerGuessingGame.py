import random

print()
print("Number Guessing Game between 1-10")
print()


def pickNumber():
    num1 = int(input("I want to guess a number between: "))
    num2 = int(input("and: "))
    guessLimit = 3
    guessCount = 0
    if num2 <= num1:
        print()
        print("[Error] Second number cannot be greater than or equal to first number")
    else:
        def numberGuess(choosenNum):
            userGuess = input("Guess the number: ")
            while int(userGuess) != int(choosenNum):
                print(choosenNum)
                userGuess = input("Guess again: ")
                print()
            playAgain = input("Correct! Would you like to play again? Y/N: ")
            if playAgain.lower() == "y":
                pickNumber()
            elif playAgain.lower() == "n":
                print("Thanks for playing!")
            else:
                print("Thanks for playing!")


        numberGuess(random.randint(num1, num2))


pickNumber()
