import random

prompt = ">"
command = "r-rock p-paper s-scissors\n"

#rock paper scissors function
def rockpaperscissors():

    options = ["r", "p", "s"]
    player = input(command + prompt)
    computer = random.choice(options)
    global counter
    counter = 0
    global comp_counter
    comp_counter = 0

#display computer results
    def result(str):
        if computer == "r":
            print("Computer: rock")

        elif computer == "s":
            print("Computer: scissors")

        elif computer == "p":
            print("Computer: paper")

  
    result(computer)


#conditions
    if player == computer:

        print("Tie bitch😆")

    elif player == "r":
        if computer == "s":
            print("rock smashes scissors\n🚀")
            counter = counter+1

        else:
            print("paper covers rock\nI know ... its dumb")
            comp_counter = comp_counter+1

    elif player == "p":
        if computer == "s":
            print("paper cuts scissors ... obv\n Dummy")
            comp_counter = comp_counter+1

        else:
            print(
                "paper on rock or something 🤷‍♀️\ncongrats! you won based on dumb logic")
            counter = counter+1

    elif player == "s":
        if computer == "r":
            print("rock destroys scissors 💥")
            comp_counter = comp_counter+1

        else:
            print("Congrats mf\n👏")
            counter = counter+1

    elif player == " ":
        print("missing input")

    elif player != options:
        print("dear gamer,\n   rock-r\n   paper-p\n   scissors-s")


#display final score
def final_result():
    print("Final Score:\n", counter, comp_counter)

    if counter > comp_counter:

        print("\n\n   Winner 🎉")

    elif counter == comp_counter:
        print("\n\n   Hmmm ... A Tie 🤔")

    else:

        print("\n\n   LOSER 👎")


#program start
print("ROCK_PAPER_SCISSORS\n")
print("best of 3 or best of 5")
best_option = ["3", "5"]
best = input(prompt)
print("dear gamer,\n   rock-r\n   paper-p\n   scissors-s")
print("happy gaming")
i = 1

# best_of conditions
if best == "3":

    while i <= 3:
        rockpaperscissors()
        i = i + 1

    final_result()


elif best == "5":
    while i <= 5:
        rockpaperscissors()
        i = i+1

    final_result()


elif best != best_option:
    print("fuck outta here")
