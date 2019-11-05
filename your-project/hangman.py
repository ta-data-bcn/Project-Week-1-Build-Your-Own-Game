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

        
    if  f.check_letter(di, mystery_word,letter, word, count_mistakes, mistake): ###Check if our letter is in the secret word
        break
    
    if count_mistakes >= mistake:                  #Check if you have the same or more mistakes than the allowed ones (dead body's pieces)
        print('You have been hang buddy....RIP')
        break

mystery_word = '*'*len(word)
print(mystery_word)
