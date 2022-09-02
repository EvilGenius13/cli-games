# flashcards.py

# import the json module from python3
# asking to input full .json name until we figure it out
import json
print("Please input which deck you would like to use? Type warcraft.json OR me-capitals.json")
input_deck = input()

warcraft = 'warcraft.json'
capitals = 'me-capitals.json'
test = 'test.json'
if input_deck == 'warcraft':
    with open((warcraft), 'r') as f:
        data = json.load(f)
elif input_deck == 'test':
    with open((test), 'r') as f:
        data = json.load(f)
else:
    with open((capitals), 'r') as f:
        data = json.load(f)


# open the file and parse the json


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

total_score = score

if total_score < 7 :
    print(f"You need practice")
else:
    print("Nice")


