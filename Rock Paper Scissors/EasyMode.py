#Easy game mode, should be mostly done for now
import random
#import Scoreboard

#make computer choice, random in easy game mode
def computer_choice_maker():
    comp_choice = random.randint(1,3)

    ch_1 = "Rock"
    ch_2 = "Paper"
    ch_3 = "Scissors"

    if comp_choice == 1:
        print "Computer chose: ", ch_1
    elif comp_choice == 2:
        print "Computer Chose: ", ch_2
    elif comp_choice == 3:
        print "Computer chose: ", ch_3

def play_game_easy():
    player_choice = int(input("Make your choice! (1 = Rock, 2 = Paper, 3 = Scissors)"))

    if player_choice == 1:
        print "You chose Rock"
    elif player_choice == 2:
        print "You chose Paper"
    elif player_choice == 3:
        print "You chose Scissors"

    #Computer's turn
    computer_choice_maker()

    #score()
    #Play again, lets user pick yes or no
    play_again = int(input("Would you like to play again? (1 = yes, 2 = no) "))

    if play_again == 1: #affirmitive
        play_game_easy()
    else:
        start_menu = int(input("Would you like to return to the main menu? (1 = yes, 2 = no) "))

        if(start_menu == 1):
            rock-paper-scissors.introduction()
        else:
            print "Goodbye!"

