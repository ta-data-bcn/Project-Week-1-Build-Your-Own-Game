#!/usr/bin/env python
# coding: utf-8

# <h1><center>Password Generator Software</center></h1>
# <h4><center>Welcome to the most secure and trusted password generator software in the world.</center></h4>

# ___________
# 
# <h2><center>Workflow and Rules</center></h2>
# 
# 
# ### Workflow
# 
# >The system will greet the user and request to answer the questions that will be used to generate the password/s.
# >
# >>The user is asked if they want to create a password, if yes, then they have to provide the length of the password and finally the number of passwords they need. 
# >>
# >>>Once the user answers all the questions the software will compute the information and will print the password/s on the screen. 
# >>>
# >>>>Finally, the user can copy-paste this password/s and use it as need it 
# 
# 
# ### Rules
# 
# 1 - The user must answer all the questions in order to get the password/s.
# 
# 2- If the user does not provide the correct information the system will let them know and it will continue to request for the right input.  

# <h2><center>Challenges and Learnings</center></h2>
# 
# #### Challenges you encountered during the process
# 
# * Working with the while loop, making sure it breaks as expected. 
# 
# #### Learnings 
# 
# * I was able to improve my knowledge on loops and Error handling.*
# 
# #### Possible future improvements
# 
# * Instead of having a single variable with the chars to create the passwords, use multiple variables one with lower letters, another with capital letters... then generate a password selecting n values from each of the variables based on the user input. 
# 
# * Create an initialize function to import the modules. 
# 
# * Import functions from a separate module. 

# <h2><center>Game Demo</center></h2>
# 

# In[1]:


import random
import time


# In[2]:


encryption = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789@#$%&?¿"


# In[3]:


def third_question():
    global n_passwords
    while True: 
        try:
            n_passwords = int(input("How many passwords do you need?: \n\n"))
            if n_passwords > 0:
                print()#uses error handling in case the value is not a number
                print(".............................................................\n")
                print(f"Ok!, let´s generate {n_passwords} passwords with a lenght of {p_len} characters\n")
                print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>GENERATING YOUR PASSWORDS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
                password_gen()
                more_passwords()
                break
            else:
                print()
                print("Please make sure you enter an integer greather than 0\n")
        except:
            print()
            print("Please enter a number\n")
        


# In[4]:


def second_question():
    global p_len
    while True:
        try:
            p_len = int(input("What lenght would you like your password to be?: \n\n"))
            print()
            if p_len > 0:
                third_question()
                break
            else: 
                print()
                print("Upss! You must enter an integer greather than 0\n")  
        except:
            print()
            print("Please enter a number\n")


# In[5]:


def initialize():

    print("                                                            PASSWORD GENERATION SOFTWARE                                            \n\n                                                 Nine out of ten computer engineers don´t recomend it. ")
    print()
    print("*******************************************************************************************************************************************")
    print()
    print("Welcome to the Password Generator Software, please answer the following questions if you want to generate extremely secure password/s.\n\n")

   
    while True:
        password_question = input("Do you need a password? Yes/No: \n\n").lower()
        print()
        if password_question == "yes":
            second_question()
            break
        elif password_question == "no":
            print()
            print("¡OH WHAT A SHAME! \n \nWell, good Luck, but be careful, your acounts might get hacked.")
            break
        else:
            print("¡Wrong Answer! Please enter Yes or No!\n")


# In[6]:


def password_gen():
    global n_passwords
    for x in range(0, n_passwords):
        password = ""
        for x in range(0, p_len):
            password_chars = random.choice(encryption)
            password = password + password_chars
            time.sleep(0.1)
        print()
        print(f"Here is your password: {password}\n")
        print("------------------------------------\n")


# In[7]:


def more_passwords():
    while True:
        more_pass = input("Do you want to generate more passwords? Yes/No: ").lower()
        print()
        if more_pass == "yes":
            second_question()
            break
        else:
            print("Thank you for using the Password Generator Software.\nWe hope all your accounts are safe with our passwords.\n")
            disclaimer()
            break


# In[8]:


def disclaimer(): 
        print("******************************************************** DISCLAIMER ****************************************************************** \n\nUse this software at your own risk, we are not liable if all your accounts are hacked.")     


# In[ ]:





# In[ ]:




