###ONBOARDING AND GIVE THE SECRET WORD 

print('Welcome to the hagnman game')
m = input('MASTER GAME, please give me the one-word: ')


##DEFINITION OF DEAD BODY TO COUNT THE MISTAKES.
mistakes = len(m) #define the maximum number of mistakes possibles according the lenght of the word.
print(mistakes)

##PLAY THE GAME
mysterious_word = '*'*len(m)
print(mysterious_word)
strings = set(m)
print(strings)
count = []
letter = input("Give me a letter and let'see if match with our secret word: ")
for i in m:
    if letter== i:
        count.append(letter)
        mysterious_word.replace('*','letter')
        print(mysterious_word)