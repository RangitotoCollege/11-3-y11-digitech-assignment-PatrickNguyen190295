import random

userName = ""
#       ITERATION 2 Start
def menu(gameChoice):
    userName = input("What is your name? ")
    while True:
        
        print(f"Welcome to the Game Room, {userName}!")
        print("1: Numskull")
        print("2: CrytoCoin")
        print("3: Dead Frequency")
        print("4: Exit")
    
        try:
            gameChoice = int(input("Choose your game (number): "))
        
            if 1 <= gameChoice <= 4:
                break
            else:
                print("Invalid Input")
        except ValueError:
            print("Invalid Input!")

    if gameChoice == 1:     # Start of Game 1
        print("You selected Numskull.")
        gameOne()
    elif gameChoice == 2:       # Start of Game 2
        print("You selected CryptoCoin.")
    elif gameChoice == 3:       # Start of Game 3
        print("You selected Dead Frequency.")
    elif gameChoice == 4:       # Exit
        print("Thank you for playing!")

    return userName

#       ITERATION 2 End

#       ITERATION 1 Start

#while True:
#    userName = input("What is your name? ")
#    print(f"Welcome to the Game Room, {userName}!")
#    print("1: Numskull")
#    print("2: CrytoCoin")
#    print("3: Dead Frequency")
#    print("4: Exit")
    
#    try:
#        gameChoice = int(input("Choose your game (number)! "))
        
#        if 1 <= gameChoice <= 4:
#            break
#        else:
#            print("Invalid Input")
#    except ValueError:
#        print("Invalid Input!")

#if gameChoice == 1:     # Start of Game 1
#    print("You selected Numskull.")
#elif gameChoice == 2:       # Start of Game 2
#    print("You selected CryptoCoin.")
#elif gameChoice == 3:       # Start of Game 3
#    print("You selected Dead Frequency.")
#elif gameChoice == 4:       # Exit
#    print("Thank you for playing!")

#       ITERATION 1 End

def gameOne():      #Game One Start
    minGuess = 1
    maxGuess = 100
    user_guess = 0
    
    print(f"Welcome, {userName}!")
    numberRan = random.randint(minGuess, maxGuess)
    print("The rule of this game, is that you have to guess the number (1-100) and I will assist you with hints along the way.")
    print("Choose Your Difficulty:")
    print("1: Easy")
    print("2: Normal")
    print("3: Hard")
    print("4: Inconceivable")
    print("5: Exit")
    while True:
        try:
            difficulty = int(input("Choose your game(number)! "))
        
            if 1 <= difficulty <= 5:
                break
            else:
                print("Invalid Input")
        except ValueError:
            print("Invalid Input!")
    if difficulty == 1:     # Start of Easy
        print("You selected Easy.")
        guess = 50
        while user_guess != numberRan and guess > 0:
            try:
                user_guess = int(input("Guess the number (1-100)"))
                guess -= 1
            except ValueError:
                print("Invalid")
    elif difficulty == 2:       # Start of Normal
        print("You selected Normal.")
        guess = 25
        while user_guess != numberRan and guess > 0:
            try:
                user_guess = int(input("Guess the number (1-100)"))
                guess -= 1
            except ValueError:
                print("Invalid")

    elif difficulty == 3:       # Start of Hard
        print("You selected Hard.")
        guess = 13
        while user_guess != numberRan and guess > 0:
            try:
                user_guess = int(input("Guess the number (1-100)"))
                guess -= 1
            except ValueError:
                print("Invalid")

    elif difficulty == 4:       # Start of Inconceivable
        print("You selected Inconceivable.")
        guess = 7
        while user_guess != numberRan and guess > 0:
            try:
                user_guess = int(input("Guess the number (1-100)"))
                guess -= 1
            except ValueError:
                print("Invalid")

    elif difficulty == 5:       # Exit
        print("Thank you for playing!")


gameChoice = 0
menu(gameChoice)
