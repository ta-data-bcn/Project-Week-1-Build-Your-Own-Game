#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##################      WELCOME TO THE GAME        ##################
import re
import functions as f


print('''
Welcome to the hangman game 
1st rule: secret names are 1-word. 
2nd rule: all secret names are low case. 
3rd rule: There are 3 levels of difficulty in function of how much mistakes has available. 
4th rule: A mistake is taken into accoun just when your fail(obvious)
5th rule : Input letters, not number nor even special characters.
''')
##################      GIVE ME A SECRET WORD       ##################
word = f.secret_word()

##################      GIVE ME THE LEVEL OF DIFFICULTY       ##################

mistake = f.difficult(word)

##################      DICTIONARY       ##################

orden = range(len(word))     ## Creation of a numbered list that I will 'zip' with the secret word( to order the word)
di = list(zip(word,orden))


##################      DEFINITION OF VALUES       ##################


count_mistakes = 0                              #Declaration of a counter the mistakes. When player will reach the maximum (pieces of deadbody), game is over.
strings =[]                                     #Empty list where we add the letters player guesses.
mystery_word = ['*' for i in range(len(word))]     #Printing of * with the same lenght as the secret_word 
#print(mystery)

##################      EXECUTION OF GAME       ##################

while (True):
    know = f.check_word()               ##ask if you want to know the secret word (yes or no)
    
    if f.guess_word(word,know):         ## function check if you guessed the secret word or not.
        break
    letter  = f.say_letter(word)        ## choose a letter to keep playing and guessing.      

        ###Check if our letter is in the secret word
    
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
            break
    else:                                  #There is no place in the secret word with the letter.
        count_mistakes += 1
        print(f'STATUS: {mystery_word}')
        print(f"this letter doesn't match with our secret word...sorry buddy!!, you have {count_mistakes} mistakes")
    print(f'You have {count_mistakes} from {mistake} mistakes \n\n\n\n\n\n')
    
    if count_mistakes >= mistake:                  #Check if you have the same or more mistakes than the allowed ones (dead body's pieces)
        print('You have been hang buddy....RIP')
        break

mystery_word = '*'*len(word)n
print(mystery_word)
