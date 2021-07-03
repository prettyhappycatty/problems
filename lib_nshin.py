
def change8to10(s):#sはString
    sum8 = 0
    j = 0
    for i in range(len(s)-1, -1, -1):
        sum8 += int(s[i])*(8**j)
        j += 1
    return sum8


def change10to9(s):#sはString
    sum9 = ""
    j = 0
    tmp = int(s)
    while tmp > 0:
        tmp1 = str(tmp % 9)
        tmp2 = tmp // 9
        sum9 = tmp1 + sum9 
        tmp = tmp2
    return sum9


def change10ton(s, n):#sはString
    sumn = ""
    j = 0
    tmp = int(s)
    while tmp > 0:
        tmp1 = str(tmp % n)
        tmp2 = tmp // n
        sumn = tmp1 + sumn 
        tmp = tmp2
    return sumn
