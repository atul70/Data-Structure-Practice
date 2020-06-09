team1 = [39,71,43,12,2,76,34]
team2 = [44,31,64,8,21,19,50]

team1.sort(reverse=False)
team2.sort(reverse=False)

print(team1, team2)
win_team1 = 0

t1_index = 0
t2_index = 0

#for i in range(0, len(team1)):
i = 0
while(i<len(team1)):
    if(team1[t1_index] > team2[t2_index]):
        win_team1 = win_team1+1
        t1_index = t1_index + 1
        t2_index = t2_index + 1
    else:
        t1_index = t1_index + 1

    i = i+1
print(win_team1)
