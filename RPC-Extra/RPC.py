import sys
from operator import truediv
from random import randint
from functions import greet, instructions, newround

#Win/Lose Colours
green = '\033[92m'
red = '\033[31m'
pink = '\033[95m'
game_state = True


#Get username
username = greet()

#Ask if want instructions
instructions()

#Win/Lose Strings
winround = (f"{green} Great job {username},you won the round!")
loseround = (f"{red} Oh no {username}, you lost the round!")

while game_state == True:
    roles = ["Rock", "Paper", "Scissors"]
    c_choice = roles[randint(0, 2)]
    u_choice = input(F'Rock, Paper, or Scissors?: ')
    game_score = 0

    if u_choice == c_choice:
        print(f"{pink}Draw!")
    if c_choice =="Rock":
        if u_choice == "Scissors":
            print(loseround)
            game_score -= 1
            
        elif u_choice == "Paper":
            print(winround)
            game_score += 1
            
    if c_choice == "Scissors":
        if u_choice == "Paper":
            print(loseround)
            game_score -= 1
            
        elif u_choice == "Rock":
            print(winround)
            game_score += 1
            
    if c_choice == "Paper":
        if u_choice == "Rock":
            print(loseround)
            game_score -= 1
            
        elif u_choice == "Scissors":
            print(winround)
            game_score += 1
            
    print(f"Your current score is {game_score}")
    game_state = newround()