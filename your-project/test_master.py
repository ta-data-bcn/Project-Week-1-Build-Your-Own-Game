print()
while True:
    n_balls = input('Enter the number of balls do you want to guess. It must be 4, 6 or 8: ')
    print()
    try:
        n_balls = int(n_balls)
        if n_balls != 4 or 6 or 8:
            print('Wrong choice. Please, select if you want to guess 4, 6 or 8 balls.')
            continue
        else:
            break
    except ValueError:
        print('This is not a valid enter. Try again.')
        continue
print('You selected to guess', n_balls, 'balls.')
print()
rsp_text = """The rules of this game are:
