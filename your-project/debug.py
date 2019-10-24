



#### DICTS VAR LISTS FUNC
### DICTIONARIES

colour_lookup = {  #consider rename to colour_converter
  "R": 0,
  "G": 1,
  "Y": 2,
  "B": 3,
  "M": 4,
  0: "R",
  1: "G",
  2: "Y",
  3: "B",
  4: "M"
}


colour_lookup_words = {
  0: "\033[0;37;41m RED ",
  1: "\033[0;37;42m GREEN ",
  2: "\033[0;30;43m YELLOW ",
  3: "\033[0;37;44m BLUE ",
  4: "\033[0;37;45m MAGENTA ",
    "R": "\033[0;37;41m RED ",
  "G": "\033[0;37;42m GREEN ",
  "Y": "\033[0;30;43m YELLOW ",
  "B": "\033[0;37;44m BLUE ",
  "M": "\033[0;37;45m MAGENTA "
}

#player_guess_nums = [] 
#colour_lookup["Y"]
#guess_var = "R"
#colour_lookup[guess_var]
#player_guess_nums = []
#player_guess_nums.append(colour_lookup[guess_var])
#print(player_guess_nums)

### VARS & Lists

code_to_crack = []
colour_letters = ["R","G","Y","B","M"]
count_black = 0
count_white = 0
game_round = 0
n_rounds= 5
player_guess= []
player_guess_nums= []
won_yet = 0


#things to import
import random

#Generic functions

def game_reset():
    global code_to_crack 
    global count_black 
    global count_white 
    global game_round
    global player_guess
    global player_guess_nums
    global rounds
    code_to_crack = []
    count_black = 0
    count_white = 0
    game_round = 0
    player_guess= []
    player_guess_nums= []
    rounds = 0

def display_welcome_message():
    print ("######################################################## ")
    print ("######## Welcome to the game of Mastermind 2019 ######## ")
    print ("######################################################## ")
    print ("In this game you'll be playing against the computer who will create a combination of 3 from a pool of 5 colours. The computer can repeat the colour selection.")
    print ("For example the computer could pick RED RED YELLOW or GREEN GREEN GREEN")
    print ("You will have 5 attempts to try and guess the correct colour and position of the computers combination")
    print (f"Remeber the options are \033[0;37;41m [R]ED \033[0;37;42m [G]REEN \033[0;30;43m [Y]ELLOW \033[0;37;44m [B]LUE \033[0;37;45m [M]AGENTA \033[0;32;97m" )
    print ("GOOD LUCK | BUENA SUERTA")
    
def cpu_code_gen():
    global code_to_crack
    code_to_crack = [random.randint(0,4), random.randint(0,4), random.randint(0,4)]  
    print (code_to_crack)

def player_guess_entry(text_to_ask):
    global player_guess_nums
    global player_guess
    while (True):
        guess_var = input(f"{text_to_ask}")
        if guess_var not in str(colour_letters):
            print("Remember to use a single character [R]ed [G]reen [Y]ellow [B]lue [M]agenta")
            continue
        else:
            player_guess_nums.append(colour_lookup[guess_var])
            player_guess.append(guess_var)
            return


def game_start():
    game_reset()
    display_welcome_message()
    cpu_code_gen()
    
    
def round_reset():
    global player_guess_nums
    global player_guess    
    player_guess = []
    player_guess_nums = []


def init_user_input():
    global game_round
    global player_guess_nums
    global player_guess
    round_reset()
    player_guess_entry("Enter your guessfor POSITION 1! Remember to use a single character [R]ed [G]reen [Y]ellow [B]lue [M]agenta : ")
    player_guess_entry("Enter your guess for POSITION 2! :")
    player_guess_entry("Enter your guess for POSITION 3! :")
    print(f"Your combination for this round is {colour_lookup_words[player_guess_nums[0]]} {colour_lookup_words[player_guess_nums[1]]} {colour_lookup_words[player_guess_nums[2]]}")
    game_round += 1



def assessment_of_player_peg(position): #pos is 0, 1, 2 and colour is RGYBM
    global count_white
    global count_black
    if player_guess_nums[position] not in code_to_crack:
        pass #get rid of this and reinstate return below
        #return print ("N")
    else:
        if player_guess_nums[position] == code_to_crack[position]: #this means colour and position are correct
            count_black += 1
            #return print ("P")
        else:
            count_white += 1 #this means colour is present somewhere in the sequence.
            #return print ("C")

def peg_score_so_far():
    global count_white
    global count_black
    print (f"This guess scored you {count_white} white pegs and {count_black} black pegs. Keep going!")
    #return
        

def assessment_of_round():
    global player_guess_nums
    global code_to_crack
    global won_yet
    assessment_of_player_peg(0)
    assessment_of_player_peg(1)
    assessment_of_player_peg(2)
    if player_guess_nums == code_to_crack:
        print("WINNER!!!")
        won_yet += 1
        #return 
    else:
        peg_score_so_far()


def game_over():
    print("Game over!")
    start_again = input(f"Do you want to start again? (Y/N) ")
    if start_again == "Y":
        game_start()


game_start()
while won_yet == 0:
    while game_round < 5:
        print(code_to_crack)
        if game_round >= 1:
            peg_score_so_far()
        init_user_input()
        print(code_to_crack)
        assessment_of_round()
        #game_over()
