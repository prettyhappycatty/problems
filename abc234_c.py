N = int(input())


def change10to2(s):#sはString
    sum9 = ""
    j = 0
    tmp = int(s)
    while tmp > 0:
        tmp1 = str(tmp % 2)
        tmp2 = tmp // 2
        sum9 = tmp1 + sum9 
        tmp = tmp2
    return sum9

print(change10to2(str(N)).replace("1","2"))
