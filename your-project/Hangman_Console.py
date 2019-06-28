import random
from pyfiglet import Figlet


# list of words and the alphabet
words = ['Encryption', 'Database', 'Algorithm', 'Cryptology', 'Python', 'Ironhack', 'Programmer']
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

tried_letters_set = set() # set of letters entered as input
guess_of_the_user = []

index = random.randint(0,len(words)-1) # random integer for the index
key_word = words[index] # our key word
key_word_as_list = []

# converting the key_word to a list called key_word_as_list
for i in range(len(key_word)):
    key_word_as_list.append(key_word[i].upper())

# prints the word in the console
def print_updated_str(user_ch):
    for i in range(len(key_word_as_list)):
        if key_word_as_list[i] == user_ch:
            guess_of_the_user[i] = user_ch

    str_to_print = ""

    for i in range(len(guess_of_the_user)):
        str_to_print = str_to_print + guess_of_the_user[i] + " "

    custom_fig = Figlet(font='standard')
    print(custom_fig.renderText(str_to_print))


# function to print the hangman
def print_hangman(fault):
    if fault == 1:
        print("""
            |
            |
            |
            |
            |
           _|_
        """)
    elif fault == 2:
        print("""
             ________
            |
            |
            |
            |
            |
           _|_
        """)
    elif fault == 3:
        print("""
             ________
            |        |
            |
            |
            |
            |
           _|_
        """)
    elif fault == 4:
        print("""
             ________
            |        |
            |        O
            |
            |
            |
           _|_
        """)
    elif fault == 5:
        print("""
             ________
            |        |
            |        O
            |        |  
            |        |   
            |
           _|_
        """)
    elif fault == 6:
        print("""
             ________
            |        |
            |        O
            |       /|\   
            |        |   
            |
           _|_
        """)
    else:
        print("""
             ________
            |        |   
            |        O
            |       /|\   
            |        |   
            |       / \  
           _|_
           
    __     ______  _    _             _____  ______    _____  ______          _____  
    \ \   / / __ \| |  | |      /\   |  __ \|  ____|  |  __ \|  ____|   /\   |  __ \ 
     \ \_/ / |  | | |  | |     /  \  | |__) | |__     | |  | | |__     /  \  | |  | |
      \   /| |  | | |  | |    / /\ \ |  _  /|  __|    | |  | |  __|   / /\ \ | |  | |
       | | | |__| | |__| |   / ____ \| | \ \| |____   | |__| | |____ / ____ \| |__| |  
       |_|  \____/ \____/   /_/    \_\_|  \_\______|  |_____/|______/_/    \_\_____/ 
                                                                               
        """)
        exit()

# driver function for the game
def play():
    custom_fig = Figlet(font='standard')
    print(custom_fig.renderText("Welcome To HANGMAN"))

    user_fault = 0
    max_fault = 7

    space = "_ " * len(key_word_as_list)
    custom_fig = Figlet(font='standard')
    print(custom_fig.renderText(space))

    for i in range(len(key_word_as_list)):
        guess_of_the_user.append("_")


    while(user_fault < max_fault):
        if(guess_of_the_user == key_word_as_list):
            custom_fig = Figlet(font='standard')
            print(custom_fig.renderText("! ! ! CONGTRATS ! ! !"))
            break
        else:
            user_ch = str(input("Enter a letter: "))
            while user_ch not in alphabet:
                user_ch = str(input("Please enter a letter: "))

            if user_ch in tried_letters_set:
                print("You have already used letter(s)" , tried_letters_set)
                user_ch = str(input("Please enter a new letter: "))
            else:
                tried_letters_set.add(user_ch)

            if user_ch in key_word_as_list:
                print_updated_str(user_ch)

            else:
                user_fault = user_fault + 1
                print_hangman(user_fault)
    return

play()
