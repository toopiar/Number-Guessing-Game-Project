import random

#Welcome Message
print("Welcome! In this game, you have a number of chances to guess a number from 1 to 100.")

#Main Game Loop
while True:
    usrInput = input("Would you like to play? (Y/N): ")

    if usrInput in ['Y', 'y']:
        #Flag for replaying the game without restarting the program
        playAgain = True

        
        print("\nGreat! Let's start the game. Choose a difficulty level:")
        
        #Game Loop: Continues until the user decides to stop playing.
        while playAgain:
            
            #Difficulty Selection
            difficultyInput = input("1. Easy (10 chances)\n2. Medium (7 chances)\n3. Hard (5 chances)\nChoice: ")

            if difficultyInput == '1':
                chances = 10
            elif difficultyInput == '2':
                chances = 7
            elif difficultyInput == '3':
                chances = 5
            
            else: #Returns to difficulty selection if input is invalid
                print("Invalid input. Please enter 1, 2, or 3.")
                continue  # back to difficulty selection

            #Number Generator and Guessing Loop
            number_to_guess = random.randint(1, 100)
            guess_counter = 0

            while guess_counter < chances:
                try:
                    user_guess = int(input("Enter your guess (1-100): "))
                
                except ValueError: #Handles non-integer inputs
                    print("Invalid input. Please enter a number.")
                    continue

                guess_counter += 1

                #Guess Evaluation
                #Exits loop if user guesses correctly
                if user_guess == number_to_guess:
                    print(f"Correct! The number was {number_to_guess}. You guessed it in {guess_counter} tries.")
                    break

                elif user_guess > number_to_guess:
                    print(f"Your guess of {user_guess} is higher! ({guess_counter}/{chances} used)")
                else:
                    print(f"Your guess of {user_guess} is lower! ({guess_counter}/{chances} used)")

            else:  # only runs if loop didn’t break (out of chances)
                print(f"You have used up all your chances! The number to guess was {number_to_guess}.")

            #Replay prompt. Program exits if input is invalid.
            replayInput = input("Would you like to play again? (Y/N): ")
            if replayInput in ['N', 'n']:
                playAgain = False
                print("Thanks for playing! Goodbye!")
                exit()
            elif replayInput not in ['Y', 'y']:
                print("Invalid input. Exiting game.")
                exit()

    #User chooses not to play at the start.
    elif usrInput in ['N', 'n']:
        print("Alright, thank you! Goodbye!")
        break

    else: #Handles invalid input at the start
        print("Invalid input, please enter Y or N.")
