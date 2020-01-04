import re

#FUNCTIONS 

#Attacker/Defendant can choose max. 9 soldiers 
#Players decide how many soldiers to play with. 
#RegEx to check if the players' input is an integer between 1 and 9.

def soldier_checker(text_to_ask):
    while True: 
        integer = input(text_to_ask)

        if re.match("^[1-9]$", integer) is not None:
            return int(integer)

        print("Has to be digits between 1 and 9.")

#Attacker can attack with a maximum of three soldiers in any case
#Always has to leave one soldier behind from the total soldiers when attacking 

def dice_attack_check(text_to_ask, soldiers_attack):
    while True: 
        integer = input(text_to_ask)
        if re.match("[1-3]$", integer) is not None:
            if int(integer) < soldiers_attack:
                return int(integer)
            elif int(integer) == soldiers_attack:
                print("You have to leave one soldier behind.")
        else:
            print("Please enter a digit between 1 and 3. Maximum of three soldiers.")

#Defender can defend with a maximum of two soldiers

def dice_defend_check(text_to_ask, soldiers_defense):
    while True: 
        integer = input(text_to_ask)
        if re.match("^[1-2]$", integer) is not None:
            if int(integer) <= soldiers_defense:
                return int(integer)
            elif int(integer) > soldiers_defense: 
                print("You don't have that many soldiers!")
        else: 
            print("Please enter a digit between 1 and 2. Maximum of 2 soldiers.")
