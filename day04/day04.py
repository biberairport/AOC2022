import re
r1 = r2 = 0

with open("day04/day04.txt", 'r') as fh:
    for x in fh:
        x = re.split('[,-]', x)
#task1
        if(int(x[0]) <= int(x[2]) and int(x[1]) >= int(x[3]) or int(x[0]) >= int(x[2]) and int(x[1]) <= int(x[3])): r1 += 1
#taks2
        if(int(x[0]) <= int(x[2]) and int(x[1]) >= int(x[2]) or int(x[0]) >= int(x[2]) and int(x[1]) <= int(x[3]) or int(x[0]) <= int(x[3]) and int(x[1]) >= int(x[3])): r2 += 1   

print(r1, r2)