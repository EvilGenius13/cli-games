# flashcards.py

# import the json module from python3
# asking to input full .json name until we figure it out
import json
# Keeps game live until loop break
game_state = True
while (game_state):
# Pick deck to use
    print("Please input which deck you would like to use?")
    print("Input : warcraft, athletes, or capitals")
    input_deck = input()

    warcraft = 'warcraft.json'
    capitals = 'me-capitals.json'
    athletes = 'athletes.json'
    # if statement to pick which deck to use
    # will open the file and parse the json
    if input_deck == 'warcraft':
        with open((warcraft), 'r') as f:
            data = json.load(f)
    elif input_deck == 'athletes':
        with open((athletes), 'r') as f:
            data = json.load(f)
    else:
        with open((capitals), 'r') as f:
            data = json.load(f)


    # score by total
    total = len(data["cards"])
    score = 0

    for i in data["cards"]:
        guess = input(i["q"] + " >")
        
        if guess.lower() == i["a"].lower():
            score += 1
            print(f"Correct! Current score: {score}/{total}")
        else:
            print(f"Incorrect! The correct answer was", i["a"])
            print(f"Current score: {score}/{total}")

    
    print(f'Your Final Score is {score} out of {total}')
    if (input(f'Would you like to play again? yes or no :') == 'yes'):
        print("Another round coming up!")
    else:
        print("Thanks for playing!")
        break
 


