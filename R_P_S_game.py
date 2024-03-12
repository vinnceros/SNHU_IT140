import random

options = ["Rock", "Paper", "Scissors"] 

# options for the game

player = False #sets player to False

print("You can type stop to terminate the program")

#The program can be stopped by typing stop.

while player == False: # While loop will take place as long as player is False
    opponent = options[random.randint(0,2)] # Sets a random value for opponent between 0,1,2 that then pulls the respective item from the list in order 0= Rock ect.

    player = input("Pick: Rock, Paper, Scissors?") # Asks player to choose / input option
    
    if player == opponent: # If the player and opponent are the same then no winner is declared
        print("No Winner, Try again.")

    elif player == "Rock": # If player chooses Rock
        if opponent == "Paper": # Paper will declare the player the loser of the round
            print("You lose,", opponent, "beats", player)
        else:# Or they are the winner
            print("You win,", player, "beats", opponent)

    elif player == "Paper": # Player picked Paper
        if opponent == "Scissors": # Scissors ends the round with the opponent winning
            print("You lose,", opponent, "beats", player)
        else:# If not Rock must have been picked by the oppenend and the player wins
            print("You win,", player, "beats", opponent)

    elif player == "Scissors":# Same with player picking Scissors
        if opponent == "Rock": # Rock for the opponent wins them the round
            print("You lose,", opponent, "beats", player)
        else:# Or the player wins
            print("You win,", player, "beats", opponent)

    elif player == "stop": break # if the player opts to stop the program will stop at this point
           
    else: # If nothing above is triggered properly then the player misspelled the word, or did not pick a correct choice and the message bellow is displayed.
        print("Input not valid. Make sure your selection was capitalized.")

    player = False # Sets player back to False, to properly restart loop and continue the game
    
