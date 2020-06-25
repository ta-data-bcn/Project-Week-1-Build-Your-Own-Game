###defining list of names of cpu_teams
def cpu_teams():
    cpu_possible_teams = ["cpu1", "cpu2","cpu3","cpu4","cpu5","cpu6"]
    cpu_teams = []
    i = 0

    for i in cpu_possible_teams:
        while len(cpu_teams) < num_cpu_teams:
            cpu_teams.append(cpu_possible_teams(i))
            i += 1
    print("The teams playing are " + user_team + " against " + cpu_teams)