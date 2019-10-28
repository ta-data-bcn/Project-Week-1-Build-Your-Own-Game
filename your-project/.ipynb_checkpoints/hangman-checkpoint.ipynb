{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "###WELCOME TO THE GAME \n",
    "import re\n",
    "\n",
    "print('Welcome to the hangman game \\n1st rule: secret names are 1-word. \\n2nd rule: all secret names are low case. \\n3rd rule: There are 3 levels of difficulty in function of how much mistakes has available. \\n4th rule: A mistake is taken into accoun just when your fail(obvious)')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "###GIVE ME A SECRET WORD\n",
    "\n",
    "m = input('MASTER GAME, please give me a secret word: ')\n",
    "m = m.lower()\n",
    "while re.match('^[a-z]+$',m) ==  None:\n",
    "    m = input('MASTER GAME, please give me A GOOD secret word : ')\n",
    "    m = m.lower() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "###GIVE ME THE LEVEL OF DIFFICULTY\n",
    "import re\n",
    "\n",
    "difficulty = (input('What is the range of difficuty you want? \\n Press (1)Easy mode, (2) Normal mode, (3) Ironhacker mode:'))    \n",
    "#print(difficulty)\n",
    "while re.match('^[1-3]$',difficulty) == None:\n",
    "    difficulty = (input('Give me a correct level of difficulty\\n Press (1)Easy mode, (2) Normal mode, (3) Ironhacker mode:'))\n",
    "    \n",
    "    ##DEFINITION DIFFICULT ODE:\n",
    "##DEAD BODY TO COUNT THE MISTAKES.\n",
    "\n",
    "\n",
    "#define the maximum number of mistakes possibles according the lenght of the word\n",
    "\n",
    "if difficulty == '1':          ##EASY MODE\n",
    "    mistakes = 2*len(m) \n",
    "    \n",
    "elif difficulty == '2':         ##NORMAL MODE\n",
    "    mistakes = len(m)\n",
    "    \n",
    "else:                         ##IRONHACK MODE\n",
    "    mistakes = int(len(m)/2)\n",
    "#print(m,difficulty,len(m), mistakes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##DICTIONARY\n",
    "\n",
    "orden = range(len(m))     ## Creation of a numbered list that I will 'zip' with the secret word( to order the word)\n",
    "di = list(zip(m,orden))\n",
    "#print(di)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##DEFINITION OF VALUES\n",
    "rounds = 0               #Declaration of # of rounds. Useful to know how the man is hang.\n",
    "count_mistakes = 0       #Declaration of a counter the mistakes. When player will reach the maximum (pieces of deadbody), game is over.\n",
    "strings =[]              #Empty list where we add the letters player guesses.\n",
    "\n",
    "#####DRAFT THE HIDDEN AND SECRET WORD BY ASTERISTICS\n",
    "mystery = ['*' for i in range(len(m))]\n",
    "print(mystery)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "##PLAY THE GAME\n",
    "while (True):\n",
    "        know = input(\"Do you know the secret word?: (y) or (n)\")\n",
    "        while re.match('^[y|n]$',know) ==  None:\n",
    "            know = input('Sorry, I do not understand, Do you know the secret word?: (y) or (n) ')\n",
    "            \n",
    "        if know == 'y':\n",
    "            trial = input('give me the secret word:')\n",
    "            trial = trial.lower()\n",
    "            if m == trial:\n",
    "                print('You win the game, CONGRATULATIONS!!!')\n",
    "                break\n",
    "            else:\n",
    "                print('No, it is not the secret word. Keep playing buddy')\n",
    "        else:\n",
    "            print('Dont worry man, just keep playing...')\n",
    "            \n",
    "        letter = input(\"Give me a letter and let'see if match with our secret word: \")\n",
    "        letter = letter.lower() \n",
    "        #make sure this is a string and letter.\n",
    "        while re.match('^[a-z]+$',m) ==  None:\n",
    "            letter = input('MASTER GAME, please give me A GOOD secret word : ')\n",
    "            letter = letter.lower() \n",
    "        count = 0 #how many letters you guess in each round. this count re-start to zero for each round (each new letter)\n",
    "\n",
    "        \n",
    "            ###Check if our letter is in the secret word\n",
    "        for i in range(len(di)):\n",
    "            #print(di[i][0],i)\n",
    "            if letter == di[i][0]:\n",
    "                mystery[di[i][1]] = letter\n",
    "                count += 1\n",
    "                pass\n",
    "        if count > 0:                           #There is one or more places in the secret word where letter matches\n",
    "            word = ''.join(mystery)\n",
    "            print(f'STATUS: {mystery}')\n",
    "            if word != m:\n",
    "                print(\"very well, you guess one letter\")\n",
    "            else:\n",
    "                print('You win the game, CONGRATULATIONS!!!')\n",
    "                break\n",
    "        else:                                  #There is no place in the secret word with the letter.\n",
    "            count_mistakes += 1\n",
    "            print(f'STATUS: {mystery}')\n",
    "            print(f\"this letter doesn't match with our secret word...sorry buddy!!, you have {count_mistakes} mistakes\")\n",
    "            rounds += 1                        #We add a mistake in the #rounds if player wrongs.\n",
    "        print(f'You are in the {rounds} round, you have {count_mistakes} from {mistakes} mistakes \\n\\n\\n\\n\\n\\n')\n",
    "        \n",
    "        if rounds >= mistakes:                  #Check if you have the same or more mistakes than the allowed ones (dead body's pieces)\n",
    "            print('You have been hang buddy....RIP')\n",
    "            break\n"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "mystery = '*'*len(m)\n",
    "print(mystery)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "strings = 'jhrhk'\n",
    "a = strings.split()\n",
    "print(a)\n",
    "temporal_word =('pnmh')\n",
    "la ='pnmh'\n",
    "if strings==temporal_word:\n",
    "    print('yes')\n",
    "    print(strings)\n",
    "else:\n",
    "    print('no')\n",
    "    print(strings)    \n",
    "if la==temporal_word:\n",
    "    print('yes')\n",
    "else:\n",
    "    print('no')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "p = ['r','s']\n",
    "print(p)\n",
    "\n",
    "t = ''.join(p)    # Union of all letters in a string to compare with the secret word\n",
    "print(t)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "strings = ['c', 's']\n",
    "b ='hola'\n",
    "#b =strings.split()\n",
    "#b = list(strings)\n",
    "print(dict(enumerate(b)))\n",
    "c = dict(enumerate(b))\n",
    "type(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "file_extension": ".py",
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  },
  "mimetype": "text/x-python",
  "name": "python",
  "npconvert_exporter": "python",
  "pygments_lexer": "ipython3",
  "version": 3
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
