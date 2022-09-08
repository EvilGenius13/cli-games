from asyncore import ExitNow


def greet():
    name = input("Hi, what's your name?: ")
    print(f"Hello {name}")
    return name

def instructions():
    response = input("Would you like to hear instructions? Yes or No: ")
    #for some reason .upper isn't working
    if response == "Yes":
        print("Pick Rock, Paper, or Scissors")
        print("Rock beats Scissors")
        print("Scissors beats Paper")
        print("Paper beats Rock")
    else: 
        print("Okay let's play!")
        

def newround():
    play_again = input("Another round? Yes or No?: ")
    if play_again == "Yes":
        return True
    else: 
        print("Thanks for playing")
        exit()

