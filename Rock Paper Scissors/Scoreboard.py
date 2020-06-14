#Scoreboard
from EasyMode import comp_choice, player_choice #fix import problem

player_score = 0
AI_score = 0

def score_board():
    #tie
    if comp_choice == player_choice:
        print "Tie"
        player_score += 1
        AI_score += 1
    #computer chooses rock
    elif comp_choice == 1 & player_choice == 3:
        print "Computer Wins!"
        AI_score += 1
    #computer chooses paper
    elif comp_choice == 2 & player_choice == 1:
        print "Computer Wins!"
        AI_score += 1
    #computer chooses paper
    elif comp_choice == 3 & player_choice == 2:
        print "Computer Wins!"
        AI_score += 1
    #player chooses rock
    elif player_choice == 1 & comp_choice == 3:
        print "You Win!"
        player_score += 1
    #player chooses paper
    elif player_choice == 2 & comp_choice == 1:
        print "You Win!"
        player_score += 1
    #player chooses scissors
    elif player_choice == 3 & comp_choice == 2:
        print "You Win!"
        player_score += 1
    