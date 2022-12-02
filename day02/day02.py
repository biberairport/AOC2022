
result = result2 = 0

with open("day02.txt", 'r') as filehandle:
    for line in filehandle:
        x = line.split()
        a = ord(x[0])-64; b = ord(x[1])-87
# task 1
        result += b
        if(a == b): result += 3
        elif(a + b == 3 and a < b or a + b == 4 and a > b or a + b == 5 and a < b): result += 6
# task 2
        if(b == 1): result2 += a - b
        if(b == 2): result2 += (a + 3)
        if(b == 3): result2 += (a + 7)
        if(a == b == 1): result2 += 3
        if(a == b == 3): result2 -= a

print(result, result2)



        