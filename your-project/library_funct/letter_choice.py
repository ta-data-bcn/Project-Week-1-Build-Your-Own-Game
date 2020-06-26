def letter_choice():
    alphabet = list(map(chr, range(97, 123)))
    letter_choice = []

    import random
    letter = random.choice(alphabet)
    letter_choice.append(letter)
    print("This rounds letter is" + letter)