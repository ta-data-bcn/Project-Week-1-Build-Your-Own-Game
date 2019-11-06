#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###WELCOME TO THE GAME 
import re

print('Welcome to the hangman game \n1st rule: secret names are 1-word. \n2nd rule: all secret names are low case. \n3rd rule: There are 3 levels of difficulty in function of how much mistakes has available. \n4th rule: A mistake is taken into accoun just when your fail(obvious)')


# In[ ]:


###GIVE ME A SECRET WORD

m = input('MASTER GAME, please give me a secret word: ')
m = m.lower()
while re.match('^[a-z]+$',m) ==  None:
    m = input('MASTER GAME, please give me A GOOD secret word : ')
    m = m.lower() 


# In[ ]:


###GIVE ME THE LEVEL OF DIFFICULTY
import re

difficulty = (input('What is the range of difficuty you want? \n Press (1)Easy mode, (2) Normal mode, (3) Ironhacker mode:'))    
#print(difficulty)
while re.match('^[1-3]$',difficulty) == None:
    difficulty = (input('Give me a correct level of difficulty\n Press (1)Easy mode, (2) Normal mode, (3) Ironhacker mode:'))
    
    ##DEFINITION DIFFICULT ODE:
##DEAD BODY TO COUNT THE MISTAKES.


#define the maximum number of mistakes possibles according the lenght of the word

if difficulty == '1':          ##EASY MODE
    mistakes = 2*len(m) 
    
elif difficulty == '2':         ##NORMAL MODE
    mistakes = len(m)
    
else:                         ##IRONHACK MODE
    mistakes = int(len(m)/2)
#print(m,difficulty,len(m), mistakes)


# In[ ]:


##DICTIONARY

orden = range(len(m))     ## Creation of a numbered list that I will 'zip' with the secret word( to order the word)
di = list(zip(m,orden))
#print(di)


# In[ ]:


##DEFINITION OF VALUES
rounds = 0               #Declaration of # of rounds. Useful to know how the man is hang.
count_mistakes = 0       #Declaration of a counter the mistakes. When player will reach the maximum (pieces of deadbody), game is over.
strings =[]              #Empty list where we add the letters player guesses.

#####DRAFT THE HIDDEN AND SECRET WORD BY ASTERISTICS
mystery = ['*' for i in range(len(m))]
print(mystery)


# In[ ]:


##PLAY THE GAME
while (True):
        know = input("Do you know the secret word?: (y) or (n)")
        while re.match('^[y|n]$',know) ==  None:
            know = input('Sorry, I do not understand, Do you know the secret word?: (y) or (n) ')
            
        if know == 'y':
            trial = input('give me the secret word:')
            trial = trial.lower()
            if m == trial:
                print('You win the game, CONGRATULATIONS!!!')
                break
            else:
                print('No, it is not the secret word. Keep playing buddy')
        else:
            print('Dont worry man, just keep playing...')
            
        letter = input("Give me a letter and let'see if match with our secret word: ")
        letter = letter.lower() 
        #make sure this is a string and letter.
        while re.match('^[a-z]+$',m) ==  None:
            letter = input('MASTER GAME, please give me A GOOD secret word : ')
            letter = letter.lower() 
        count = 0 #how many letters you guess in each round. this count re-start to zero for each round (each new letter)

        
            ###Check if our letter is in the secret word
        for i in range(len(di)):
            #print(di[i][0],i)
            if letter == di[i][0]:
                mystery[di[i][1]] = letter
                count += 1
                pass
        if count > 0:                           #There is one or more places in the secret word where letter matches
            word = ''.join(mystery)
            print(f'STATUS: {mystery}')
            if word != m:
                print("very well, you guess one letter")
            else:
                print('You win the game, CONGRATULATIONS!!!')
                break
        else:                                  #There is no place in the secret word with the letter.
            count_mistakes += 1
            print(f'STATUS: {mystery}')
            print(f"this letter doesn't match with our secret word...sorry buddy!!, you have {count_mistakes} mistakes")
            rounds += 1                        #We add a mistake in the #rounds if player wrongs.
        print(f'You are in the {rounds} round, you have {count_mistakes} from {mistakes} mistakes \n\n\n\n\n\n')
        
        if rounds >= mistakes:                  #Check if you have the same or more mistakes than the allowed ones (dead body's pieces)
            print('You have been hang buddy....RIP')
            break

mystery = '*'*len(m)
print(mystery)
# In[ ]:


strings = 'jhrhk'
a = strings.split()
print(a)
temporal_word =('pnmh')
la ='pnmh'
if strings==temporal_word:
    print('yes')
    print(strings)
else:
    print('no')
    print(strings)    
if la==temporal_word:
    print('yes')
else:
    print('no')


# In[ ]:


p = ['r','s']
print(p)

t = ''.join(p)    # Union of all letters in a string to compare with the secret word
print(t)


# In[ ]:


strings = ['c', 's']
b ='hola'
#b =strings.split()
#b = list(strings)
print(dict(enumerate(b)))
c = dict(enumerate(b))
type(c)


# In[ ]:




