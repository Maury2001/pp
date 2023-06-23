import random

prompt = ">"
options = ["rock", "paper", "scissors"]
print("ROCK PAPER SCISSORS\n")
player = input(prompt)
computer = random.choice(options)

print(player, computer)

if player == computer:
    print('tie')

elif player == "rock":
    if computer=="scissors":
        print("rock smashes scissors >>> looseer")
    else:
        print("paper covers rock >>> dont ask me how thats just how it is") 

elif player == "scissors":
     if computer=="rock":
        print("rock smashes scissors >>> bozoo")
     else:
        print("scissors cut paper >>> obv")
        

elif player =="paper":
     if computer=="scissors":
        print("scissors cut paper >>> dumbass")
     else:
        print("paper covers rock >>> stupid i know")



 