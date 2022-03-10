T = int(input())

def change10to2(s):#sはString
    sum9 = ""
    j = 0
    tmp = int(s)
    while tmp > 0:
        tmp1 = str(tmp % 2)
        tmp2 = tmp // 2
        sum9 = tmp1 + sum9 
        tmp = tmp2
    return str(sum9)

def change2to10(s):#sはString
    sum8 = 0
    j = 0
    for i in range(len(s)-1, -1, -1):
        sum8 += int(s[i])*(2**j)
        j += 1
    return sum8

def check(an):
    for i in range(len(an)):
        #print(an[i])
        if change2to10(an[i][0]) + change2to10(an[i][1]) == a:
            return True
    return False

# x AND y = a
# x + y = (x XOR y) + 2*(x AND y) = s
#          x XOR y + 2*a = s
#          x XOR y = s - 2*a #どちらかが1

def check(stror, strand):
    for j in range(len(str2xxory)):
        if str2xxory[j] == 1 and str2xandy == 1:
            return False
    return True

for i in range(T):
    a, s = map(int, input().split())
    x_and_y = a
    #print(change10to2(str(a)))
    x_xor_y = s - 2*a

    str2xandy = change10to2(str(x_and_y))
    if x_xor_y >= 0:
        str2xxory = change10to2(str(x_xor_y))
        #print(len(str2xandy),len(str2xxory))
        if len(str2xandy)   > len(str2xxory):
            str2xxory = "0"*(len(str2xandy)-len(str2xxory)) + str2xxory
        else:
            str2xandy = "0"*(len(str2xxory)-len(str2xandy)) + str2xandy
        if check(str2xxory,str2xandy):
            print("Yes")
        else:
            print("No")
    else:
        print("No")

