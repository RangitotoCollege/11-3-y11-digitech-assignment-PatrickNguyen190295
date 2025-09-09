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

difOne = "Uncompleted"
difTwo = "Uncompleted"
difThree = "Uncompleted"
difFour = "Uncompleted"

def gameOne():      #Game One Start

    global userName
    global difOne
    global difTwo
    global difThree
    global difFour

    minGuess = 1
    maxGuess = 100
    user_guess = 0
    
    
    print(f"Welcome, {userName}!")
    numberRan = random.randint(minGuess, maxGuess)
    print("The rule of this game, is that you have to guess the number (1-100) and I will assist you with hints along the way.")
    print("Choose Your Difficulty:")
    print(f"1: Easy ({difOne})")
    print(f"2: Normal ({difTwo})")
    print(f"3: Hard ({difThree})")
    print(f"4: Inconceivable ({difFour})")
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
        guess = 20
        maxGuess = guess
        while user_guess != numberRan and guess > 0:
            print("     ")
            try:
                
                print(f"Guesses remaining: {guess}")
                guess -= 1
                user_guess = int(input("Guess the number (1-100)"))
                if user_guess > numberRan:
                    print("Your guess was too high!")
                    
                elif user_guess < numberRan:
                    print("Your guess was too low!")
                else:
                    print(f"You won in {maxGuess - guess} guesses ")
                    difOne = "Completed"
                while leaving != "1" and leaving != "2":
                    print("1: Continue")
                    print("2: Leave")
                    leaving = input("Continue or Leave?")
                if leaving == 1:
                    gameOne()
                else:
                    menu()
                                              
            except ValueError:
                print("Invalid")

    elif difficulty == 2:       # Start of Normal
        print("You selected Normal.")
        guess = 10
        maxGuess = guess
        while user_guess != numberRan and guess > 0:
            print("     ")
            try:
                
                print(f"Guesses remaining: {guess}")
                guess -= 1
                user_guess = int(input("Guess the number (1-100)"))
                if user_guess > numberRan:
                    print("Your guess was too high!")
                    
                elif user_guess < numberRan:
                    print("Your guess was too low!")
                else:
                    print(f"You won in {maxGuess - guess} guesses ")
                    difTwo = "Completed"
                    gameOne()
                                              
            except ValueError:
                print("Invalid")    
                

    elif difficulty == 3:       # Start of Hard
        print("You selected Hard.")
        guess = 5
        maxGuess = guess
        while user_guess != numberRan and guess > 0:
            print("     ")
            try:
                
                print(f"Guesses remaining: {guess}")
                guess -= 1
                user_guess = int(input("Guess the number (1-100)"))
                if user_guess > numberRan:
                    print("Your guess was too high!")
                    
                elif user_guess < numberRan:
                    print("Your guess was too low!")
                else:
                    print(f"You won in {maxGuess - guess} guesses ")
                    difThree = "Completed"
                    gameOne()
                                              
            except ValueError:
                print("Invalid")    
                

    elif difficulty == 4:       # Start of Inconceivable
        print("You selected Inconceivable.")
        guess = 3
        maxGuess = guess
        while user_guess != numberRan and guess > 0:
            print("     ")
            try:
                
                print(f"Guesses remaining: {guess}")
                guess -= 1
                user_guess = int(input("Guess the number (1-100)"))
                if user_guess > numberRan:
                    print("Your guess was too high!")
                    
                elif user_guess < numberRan:
                    print("Your guess was too low!")
                else:
                    print(f"You won in {maxGuess - guess} guesses ")
                    difFour = "Completed"
                    gameOne()
                                              
            except ValueError:
                print("Invalid")    
                
    elif difficulty == 5:       # Exit
        print("Thank you for playing!")
        gameChoice = 0
        menu(gameChoice)

def gameTwo():
    



gameChoice = 0
menu(gameChoice)

gameChoice = 0
menu(gameChoice)
