s = "57"

def change10to2(s):#sはString
    sum2 = ""
    j = 0
    tmp = int(s)
    while tmp > 0:
        tmp1 = str(tmp % 2)
        tmp2 = tmp // 2
        sum2 = tmp1 + sum2 
        tmp = tmp2
    return sum2

print(change10to2(s))