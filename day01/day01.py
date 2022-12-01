a = b = c = d = 0

with open("day01.txt", 'r') as filehandle:
    for line in filehandle:
        if(line != "\n"):
            a += int(line)
        else:
            if(b < a): b = a
            if(c < b): a = b; b = c; c = a
            if(d < c): a = c; c = d; d = a
            a = 0

print (d)           # solution 1
print (b+c+d)       # solution 2