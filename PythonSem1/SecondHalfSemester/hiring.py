def cost(candidates):
    totalcost = 0
    for i in range(0, len(candidates)):
        totalcost = totalcost + candidates[i][1]
    return totalcost

def skills(candidates):
    skill_layout = []
    for i in range(0, len(candidates)):
        for j in range(0,len(candidates[i][0])):
            if candidates[i][0][j] not in skill_layout:
                skill_layout.append(candidates[i][0][j])
    return skill_layout

def uncovered(project, skills):
    noskills = []
    if len(skills) > 0:
        for i in range (0, len(project)):
            if project[i] not in skills:
                noskills.append(project[i])
        return noskills
    return project

def team_of_best_individuals(project, candidates):
    best_team = []

    #looping until no more skills required
    while len(uncovered(project,skills(best_team))) > 0:
        best_individual = best_individual_candidate(project,candidates)
        best_team.append(best_individual)
        candidates.remove(best_individual)
        project = uncovered(project, skills(best_team))

    for i in range (0, len(best_team)):
        best_team[i] = best_team[i][2]
    return best_team

def best_individual_candidate(project, candidates):
    bestvalue = 0
    for i in range(0, len(candidates)):
        #print(i, bestvalue)
        if comparing_individuals(candidates[i],candidates[bestvalue],project):
            bestvalue = i
    #print('finish one search')
    return candidates[bestvalue]

def comparing_individuals(normie, bestie, project):
    normielen = 0
    bestielen = 0

    for i in range(0, len(normie[0])):
        if normie[0][i] in project:
            normielen+=1

    for j in range(0, len(bestie[0])):
        if bestie[0][j] in project:
            bestielen+=1

    #print('normielen = ' , normielen)
    #print('bestielen = ', bestielen)
    #print('-')
    if normielen != 0 and (bestielen == 0 or normie[1]/normielen <  bestie[1]/bestielen):
        #print('switching bestie')
        return True

    return False

def mincost(candidates):
    min = 10000
    if candidates != []:
        for i in range (len(candidates)):
            if candidates[0][i][0][1] < min:
                min = candidates[i][1]

    return min

def best_team(project, candidates):
    if len(project) == 0:
        return []
    if len(candidates) == 0:
        print('t')
        return None

    solutions = []

    for i in range(len(candidates)):
        selectcandidate = candidates[i]

        uncovered_tasks = uncovered(project, selectcandidate[0])

        if len(uncovered_tasks) < len(project):

            #if this person has value to the project, go deeper

            subsolution = best_team(uncovered_tasks, candidates[i+1:])
            #print(subsolution)
            #if there are no subsolutions, continue the loop
            if subsolution == None:
                continue

            solutions.append([selectcandidate] + solutions)

    print(solutions)
    solutions = mincost(solutions)

    return solutions

skill_list = ["MATLAB", "STATISTICS", "PYTHON", "TENSORFLOW", "MARKETING", "SALES", "MYSQL", "WEBDESIGN", "ROBOTICS", "PHP"]
tracy = [[skill_list[0], skill_list[1], skill_list[2], skill_list[3]], 900,'tracy']
sandy = [[skill_list[4], skill_list[5]], 450,'sandy']
superman = [[skill_list[2], skill_list[6], skill_list[4], skill_list[7], skill_list[8]], 2000,'superman']
daisy = [[skill_list[6], skill_list[4]], 700,'daisy']
matt = [[skill_list[2], skill_list[9], skill_list[7]], 300,'matt']

candidates = [tracy,sandy,superman,daisy,matt]

project = [skill_list[1], skill_list[3], skill_list[0],skill_list[7]]

print(team_of_best_individuals(project,candidates))