
import re

##################      GIVE ME A SECRET WORD       ##################
#Definition of a function that request a word to play. Error handling is implemented in order to ask for just an only word 
#with no number nor special characters.


def secret_word():
    word = input('MASTER GAME, please give me a secret word: ')
    word = word.lower()
    while re.match('^[a-z]+$',word) ==  None:
        word = input('MASTER GAME, please give me a secret word, but can not be a number nor special character: ')
        word = word.lower()
    return  word

##################      GIVE ME THE LEVEL OF DIFFICULTY       ##################
#Definiton of funcion that ask for the difficulty level.  There are 3 different level that depending on the number of mistakes 
#according the number of letters has the secret word.


def difficult(word):
    difficulty = (input('What is the range of difficuty you want? \n Press (1)Easy mode, (2) Normal mode, (3) Ironhacker mode:'))    

    while re.match('^[1-3]$',difficulty) == None:
        difficulty = (input('Give me a correct level of difficulty\n Press (1)Easy mode, (2) Normal mode, (3) Ironhacker mode:'))

    #define the maximum number of mistakes possibles according the lenght of the word

    if difficulty == '1':          ##EASY MODE
        mistake = 2*len(word) 
    elif difficulty == '2':         ##NORMAL MODE
        mistake = len(word)
    else:                           ##IRONHACK MODE
        mistake = len(word)/2
    
    return mistake

##################      GIVE ME THE LEVEL OF DIFFICULTY       ##################


def check_word():
    know = input("Do you know the secret word?: (y) or (n)")
    while re.match('^[y|n]$',know) ==  None:
        know = input('Sorry, I do not understand, Do you know the secret word?: (y) or (n) ')
    return know


def guess_word(word,know):
        if know == 'y':
            trial = input('give me the secret word:')
            trial = trial.lower()
            if word == trial:
                print('You win the game, CONGRATULATIONS!!!')
                return True
            else:
                print('No, it is not the secret word. Keep playing buddy')
                return False
        else:
            print('Dont worry man, just keep playing...')
            return False

def  say_letter(word):
    letter = input("Give me a letter and let'see if match with our secret word: ")
    letter = letter.lower() 
    #make sure this is a string and letter.
    while re.match('^[a-z]+$',word) ==  None:
        letter = input('MASTER GAME, please give me A GOOD secret word : ')
        letter = letter.lower() 
    return letter 

def check_letter(di, mystery_word,letter,word,count_mistakes,mistake):
    count = 0 #how many letters you guess in each round. this count re-start to zero for each round (each new letter)   
    for i in range(len(di)):
         #print(di[i][0],i)
        if letter == di[i][0]:
            mystery_word[di[i][1]] = letter
            count += 1
            pass
    if count > 0:                           #There is one or more places in the secret word where letter matches
        checking_letter = ''.join(mystery_word)
        print(f'STATUS: {mystery_word}')
        if checking_letter != word:
            print("very well, you guess one letter")
        else:
            print('You win the game, CONGRATULATIONS!!!')
            return True
    else:                                  #There is no place in the secret word with the letter.
        count_mistakes += 1
        print(f'STATUS: {mystery_word}')
        print(f"this letter doesn't match with our secret word...sorry buddy!!, you have {count_mistakes} mistakes")
    print(f'You have {count_mistakes} from {mistake} mistakes \n\n\n\n\n\n')
    