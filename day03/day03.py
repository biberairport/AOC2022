with open("day03/day03.txt", 'r') as filehandle:    
    res = 0
    for line in filehandle:        
        x = len(line)
        a = sorted(line[:len(line)//2])
        b = sorted(line[len(line)//2:-1])
        c = ""

        for i in a:
            if(i in b and c != i):
                c = i
                if i.islower(): res += ((ord(i)-96))
                else: res += ord(i)-38
    print(res)

    filehandle.seek(0,0)
    bag = filehandle.read().splitlines()
    res = 0

    for i in range(0, len(bag), 3):
        for x in bag[i]:
            if x in bag[i+1] and x in bag[i+2]:
                if x.islower(): res += ord(x)-96; break
                else: res += ord(x)-38; break
    print(res)