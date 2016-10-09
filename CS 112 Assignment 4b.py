#Program: 4b
#Names: Walter, John Diaz
#Date: 10/06/2016
#Instructor: Jeff Light
#Description: A guessing game. User must guess a random number between 1-100.

import random

def main(): 
    #entire game under this while loop
    while True:
        tries = 0
        ranNum = random.randint(1,100)
        print ("I am thinking of a number between 1 and 100.")
        #reject anything that is not a number. Loops until user guesses correct #
        while True:
            print ("What is your guess?")
            guess = input()  
            if not(guess.isdigit()):
                print ("Enter a number, you dummy!")
                continue
            guess = int(guess)
            tries += 1       
            if guess > ranNum:
                print ("That is too high.")
            elif guess < ranNum:   
                print ("That is too low.")    
            elif guess == ranNum:
                print ("You got it in " + str(tries) + "!")   
                break
        #rejects anything not Y or N.            
        print ("Would you like to play again (Y or N)?")
        while True:
            
            playAgain = input()
            if playAgain == "Y":
                main()
            elif playAgain == "N":
                print ("Thanks for playing!")
                break
            else:
                print ("Huuuuuhhh?????")
                continue
        #this break ends the game
        break
    
if __name__ == '__main__':
    main()  #excucte main function
