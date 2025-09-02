import random

def gameOne():      #Game One Start
    minGuess = 1
    maxGuess = 100
    
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
        while userGuess != numberRan:
            try:
                userGuess = int(input("Guess the number (1-100)"))
            except ValueError:
                print("Invalid")
    elif difficulty == 2:       # Start of Normal
        print("You selected Normal.")
        guess = 25
    elif difficulty == 3:       # Start of Hard
        print("You selected Hard.")
        guess = 13
    elif difficulty == 4:       # Start of Inconceivable
        print("You selected Inconceivable.")
        guess = 7
    elif difficulty == 5:       # Exit
        print("Thank you for playing!")

def menu(gameChoice):
    while True:
    userName = input("What is your name? ")
    print(f"Welcome to the Game Room, {userName}!")
    print("1: Numskull")
    print("2: CrytoCoin")
    print("3: Dead Frequency")
    print("4: Exit")
    
    try:
        gameChoice = int(input("Choose your game (number)! "))
        
        if 1 <= gameChoice <= 4:
            break
        else:
            print("Invalid Input")
    except ValueError:
        print("Invalid Input!")

#if gameChoice == 1:     # Start of Game 1
 #   print("You selected Numskull.")
#elif gameChoice == 2:       # Start of Game 2
#    print("You selected CryptoCoin.")
#elif gameChoice == 3:       # Start of Game 3
#    print("You selected Dead Frequency.")
#elif gameChoice == 4:       # Exit
#    print("Thank you for playing!")
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
