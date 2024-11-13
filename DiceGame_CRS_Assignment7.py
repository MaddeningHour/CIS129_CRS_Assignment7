#Christopher Robles Serrano
#Module 7 Assignment CIS-129
#11/12/2024
#This program creates 2 players and simulates a random dice roll 1-6 for the players. Prints the winner(s), names, and numbers rolled.


#Importing from random to use randint
from random import *


def main():
    print("Welcome to my dice game!")
    
    #Variable to keep looping our program.
    loopProgram = "yes"

    #Assigning two variables to our inputNames function
    playerOne,playerTwo = inputNames()

    #Loops the program until the user says 'no'.
    while loopProgram == 'yes':
        #Checking to see our variables are empty. If they are they are assigning Player 1 and Player 2 respectively.
        if not playerOne.strip():
            playerOne = 'Player 1'
        if not playerTwo.strip():
            playerTwo = 'Player 2' 
        
        #Assigning 3 variables to the rollDice function. With this we know who won and what our players rolled
        p1Roll, p2Roll, winnerName = rollDice(playerOne, playerTwo)
        
        #Printing our results and an empty print statement for cleaner presentation
        displayInfo(winnerName, playerOne, playerTwo, p1Roll, p2Roll)
        print()

        #Asking the user if they want to loop the program again and converting to lowercase.
        loopProgram = input("Play again? (yes or no)").lower()

        #Loops over the our user input until they respond with "yes" or "no" to the play again question.
        while loopProgram not in ['yes','no']:
            print()
            print("Answer must be 'yes' or 'no'")
            loopProgram = input("Play again? (yes or no)").lower()
        print()
        

def inputNames():
    #Grabbing player names from the user and returning the names.
    playerOne = input("Enter player 1 name: ")
    playerTwo = input("Enter player 2 name: ")
    return playerOne, playerTwo


def rollDice(player1, player2):
    #Simulate a random dice roll for each player
    p1Roll = randint(1,6)
    p2Roll = randint(1,6)

    #Checking for winner and assinging winnerName to player
    if p1Roll > p2Roll:
        winnerName = player1

    #Checking for winner and assinging winnerName to player
    elif p2Roll > p1Roll:
        winnerName = player2

    #Assigning winnerName to 'tie' if the players rolled the same answer
    else:
        winnerName = "tie"

    return p1Roll, p2Roll, winnerName


def displayInfo(winnerName, p1Name, p2Name, p1Roll, p2Roll):
    #Printing the winner(s), names, and what the players rolled
    print(f"TIE! {p1Name} and {p2Name} both rolled {p1Roll}" if winnerName == "tie" else f'The winner is {winnerName}!\n{p1Name} rolled {p1Roll}\n{p2Name} rolled {p2Roll}')


#Calling main function    
main()