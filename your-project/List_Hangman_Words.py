#!/usr/bin/env python
# coding: utf-8

# In[6]:


def cpu_choice(): 
#List of the words used by the computer to use during the game
    words = ["yellow","elephant","red","lunch","dog","pet","dolphin"]
#The computer picks a word, converst the word onto a list with the different letters and displays the lenght
    import random
    word_choice = random.choice(words)
    return word_choice

