# At the beginning of the file I import the external libraries I'm going to use.
import datetime

# Dictionary definition with the type of levels and it's number range
levels = {  "easy" : (4, 0, 10), "medium" : (7, 0, 100), "hard" : (10, -500, 500) }
# Dictionary definition about how many tries the user have per level
tries = { "easy" : 4, "medium" : 7, "hard" : 10}


#test = [v[0] for (k,v) in levels.items() if k=="medium"]
#print(str(test).strip('[]'))

def get_username(option):
    
    if option == 1:
        username = input('What\'s your name? ') 
        print(f'Thank\'s for playing Guess the Number, {username.capitalize()}')
        get_level()
    else:
        username = input('What\'s the name of the new player? ')
        print(f'Thank\'s for playing Guess the Number, {username.capitalize()}')
        #get_menu()
    

def get_level():
    print(f'Now you have to choose a level, \nWrite 1 or easy: {levels["easy"][0]} tries and the number goes from from {str(levels["easy"][1])} to {str(levels["easy"][2])} \nWrite 2 or medium: {levels["medium"][0]} tries and the number goes from {str(levels["medium"][1])} to {str(levels["medium"][2])}\nWrite 3 or hard: {levels["hard"][0]} tries and the number goes from {str(levels["hard"][1])} to {str(levels["hard"][2])}')
    user_level = input()
    if user_level == 1:
        
        print('Okay, I have my number thought)
    elif user_level == 2:

    elif user_level == 3:
    
    else:

    get_number()
            
def get_number():
    number = input('Which number are you thinking? ')




get_username(1)