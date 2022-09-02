# cli=games/bnc.py
# Import the random method from the randint module
# cowboy eats ninja, still some errors. need to rewrite potentially to understand.
from random import randint

# Define roles including score for user and computer
roles = ["Bear", "Ninja", "Cowboy"]
# player score goes up 1 on win, down 1 on loss
player_score = 0
# Generate a random role using an array
computer = roles[randint(0,2)]
print("Get ready to play Bear, Ninja, Cowboy!")
# instructions option can also skip
if (input(f'Would you like instructions on how to play? enter yes/no: ') == 'yes'):
    print("""
    Bear, Ninja, Cowboy is an exciting game of strategy and skill! 
    Pit your wit against the computer! Choose a player: Bear, Ninja, or Cowboy. 
    The computer chooses a player. Bear eats Ninja, Ninja defeats Cowboy and cowboy shoots bear.""")
else:
    print("Let's Start!")

# keeps the game in a live state and looping unless broken
game_state = True
while (game_state):

# Get player input
    player = input("Bear, Ninja, or Cowboy > ")

    if computer == player:
        print("DRAW!")
    elif computer == "Cowboy":
        if player == "Bear":
            player_score -= 1
            print(f'You lose! {player} is shot by {computer}')
        else: # computer is cowboy, player is ninja
            player_score += 1
            print(f'"You win! {player} defeats {computer}')
    elif computer == "Bear":
        if player == "Cowboy":
            player_score += 1
            print(f'You win! {player} shoots {computer}')
        else: # computer is bear, player is ninja
            player_score -= 1
            print(f'You lose! {player} is eaten by {computer}')
    elif computer == "Ninja":
        if player == "Cowboy":
            player_score -= 1
            print(f'You lose! {player} is defeated by {computer}')
        else: # computer is ninja, player is bear
            player_score += 1
            print(f'You win! {player} eats {computer}')

# play again request 
    print(f"Your current score is : {player_score}")
    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
        game_state = True
        computer = roles[randint(0,2)]
    else:
        print(f"Your final score is {player_score}")
        break