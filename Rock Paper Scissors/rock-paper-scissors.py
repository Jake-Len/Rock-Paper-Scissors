import random
import HardMode
import EasyMode

#Intro function, gets user input of game start, instructions, and game mode
def introduction():
    like_to_play = int(input ("Welcome to Rock Paper Scissors, would you like to play? (1 = yes, 2 = no) "))
    #like_to_play = int(like_to_play)
    #need to set y/n variables instead of numeric: flow control
    
    if(like_to_play == 1):
        easy_or_hard = input("Easy (1) or hard (2)? ")
        easy_or_hard = int(easy_or_hard)

        if easy_or_hard == 1:
            EasyMode.play_game_easy()
        elif easy_or_hard == 2:
            HardMode.play_game_hard()
        else:
            print("Invalid option!")

    else:
        print("Goodbye!")

introduction()

