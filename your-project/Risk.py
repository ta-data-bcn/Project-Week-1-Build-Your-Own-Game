
import random 

import Funcs.functions as f

#Game starts

soldiers_attack = f.soldier_checker("Attacker: How many soldiers do you have? ")
soldiers_defense = f.soldier_checker("Defendant: How many soldiers do you have? ")

#Battle starts 

round_num = 1
while soldiers_attack > 1 and soldiers_defense > 0:

    print(f"Round: {round_num}") 
    
    dice_attack = f.dice_attack_check("Attacker: How many dices do you want to attack with? ", soldiers_attack)
    dice_defend = f.dice_defend_check("Defender: How many dices do you want to defend with? ", soldiers_defense)

    attacker_dices = []
 
    while len(attacker_dices) < dice_attack: 
        i = random.randint(1,6)
        attacker_dices.append(i)
    print(f"Throw for attacker: {attacker_dices}")

    defendant_dices = []
 
    while len(defendant_dices) < dice_defend: 
        i = random.randint(1,6)
        defendant_dices.append(i)
    print(f"Throw for defendant: {defendant_dices}")
    
    
    while len(defendant_dices) > 0 and len(attacker_dices) > 0:
        if max(attacker_dices) > max(defendant_dices): 
            print("Attacker wins: defendant looses one soldier")
            soldiers_defense -= 1
        else: 
            print("Defendant wins: attacker looses one soldier")
            soldiers_attack -= 1
        attacker_dices.remove(max(attacker_dices))
        defendant_dices.remove(max(defendant_dices))
        print(f"Soldiers remaining for defense: {soldiers_defense}")
        print(f"Soldiers remaining for attack: {soldiers_attack}")

    round_num += 1
       
if soldiers_attack == 1: 
    print("Game over: Attacker only has one soldier left. Defendant wins")
if soldiers_defense == 0: 
    print("Game over: Defendant has no soldiers left. Attacker wins")







