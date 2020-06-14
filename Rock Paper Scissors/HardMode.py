#hard game mode
import random

past_player_choices = [] #storing past player choices
past_computer_choices = [] #storing past computer choices

#in hard mode, past choices are stored and evaluated to check for biases toward a certain choice.
#the computer checks to see if the player uses one choice more than others and changes its play appropriately.
def play_game_hard():
    player_choice = int(input("Make your choice! (1 = Rock, 2 = Paper, 3 = Scissors)"))

    if player_choice == 1:
        print "You chose Rock"
        past_player_choices.append(player_choice)
    elif player_choice == 2:
        print "You chose Paper"
        past_player_choices.append(player_choice)
    else:
        print "You chose Scissors"
        past_player_choices.append(player_choice)
        #appending to player choices works fine.

#Computer's turn
    past_choice_maker()
    #score()
#Play again, lets user pick yes or no
    play_again = int(input("Would you like to play again? (1 = yes, 2 = no) "))

    if play_again == 1:
        play_game_hard()
    else:
        start_menu = int(input("Would you like to return to the main menu? (1 = yes, 2 = no) "))

        if(start_menu == 1):
            introduction()
        else:
            print "Goodbye!"

#Generate info on past choices to find patterns/most used choices so computer can learn. (markov algorithm)
def past_choice_maker():
    ch_1 = "Rock"
    ch_2 = "Paper"
    ch_3 = "Scissors"

    rocks = 0
    papers = 0
    scissors = 0

    if len(past_player_choices) == 0:
        comp_choice = ch_1 #default to rock if there is not bias to base moves off of
    elif len(past_player_choices) != 0:
        #establish biases
        for choice in past_player_choices:
            if choice == 1:
                rocks += 1
            elif choice == 2:
                papers += 1
            elif choice == 3:
                scissors += 1
            
        if rocks > scissors & rocks > papers:
            comp_choice = ch_2#paper
            past_computer_choices.append(comp_choice)
            print "Computer chose Paper!"
            print past_player_choices
            print rocks, papers, scissors

        elif papers > scissors & papers > rocks:
            comp_choice = ch_3#scissors
            past_computer_choices.append(comp_choice)
            print "Computer chose Scissors!"
            print past_player_choices
            print rocks, papers, scissors

        elif scissors > rocks & scissors > papers:
            comp_choice = ch_1 #rock
            past_computer_choices.append(comp_choice)
            print "Computer chose Rock!"
            print past_player_choices
            print rocks, papers, scissors


#fix: not printing if using else statement
#always using default otherwise