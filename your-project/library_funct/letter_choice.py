#defining letter choice
def letter_choice():

    alphabet = list(map(chr, range(97, 123)))
    letter_choice = []

    import random
    choosing_player = random.choice(players)

    if choosing_player in cpu_teams:
        print(choosing_player + " choose!")
        letter = random.choice(alphabet)
        letter_choice.append(letter)
        print("This rounds letter is" + letter)

    else:
        letter_player = input("You choose! What letter will be? ")
        print(letter_player)
        if letter_choice.lower() in alphabet:
            letter_choice.append(letter_player)
        else:
            print(input("You choose! What letter will be? "))