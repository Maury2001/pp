from sys import exit

def gold_room():
    print ("This room is full of gold. How much do you take?")

    next = input("> ")

    if "0" in next or "1" in next :
        how_much = int(next)

    else:
        dead ("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)

    else:
        dead("you greedy bastard")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey")
    print("The fat bear is in front of another door")
    print("How are you going to move the bear")

    options ="""
    taunt bear oor take honey
    """
    print(options)

    bear_move = False

    while True:
        next = input("> ")

        if next == "take honey":
            dead ("The bear looks at you then slaps your face off")
            break

        elif next == "taunt bear" and not bear_move:
            print("The bear has gone through the door. You can go through it now")
            bear_move = True

            break

        elif next == "taunt bear" and bear_move: 
            dead("The bear gots pissed off and chews your legs off.")
            break

        elif next == "open door" and bear_move:
            gold_room()

        else:
            print
            

def cthulhu_room():
    print("Here you see the great evil cthulhu")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat head?")

    next = input("> ")

    if "flee" in next:
        start()

    elif "head" in next:
        dead("Well that was tasty")

    else:
        cthulhu_room

def dead(why):
    print(why, "Good job")
    exit(0)

def start():
    print("You're in a dark room")
    print("There is a doctor at your right and left")
    print("Which one do you take?")

    next = input("> ")

    if next == "left":
        bear_room()

    elif next == "right":
        cthulhu_room()

    else:
        dead("you stumble around the room until you starve.")


start()






















''