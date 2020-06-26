##defining number of teams playing
def teams_num():
    num_cpu_teams = 0
    while num_cpu_teams == 0 or num_cpu_teams > 6:
        x = int(input("How many teams will you play against from 1 to 6? "))
        print(x)
        if x.isdigit():
            num_cpu_teams = x
        else:
            print(x)
    
    num_teams = num_cpu_teams + 1
    print("Then, the game will have " + str(num_teams) + " teams!")