import re
r1 = r2 = 0

with open("day04/day04.txt", 'r') as fh:
    for x in fh:
        x = (list(map(int,re.split('[,-]', x))))
#task1
        if(x[0] <= x[2] and x[1] >= x[3] or x[0] >= x[2] and x[1] <= x[3]): r1 += 1
#taks2
        if(x[0] <= x[2] and x[1] >= x[2] or x[0] >= x[2] and x[1] <= x[3] or x[0] <= x[3] and x[1] >= x[3]): r2 += 1   

print(r1, r2)