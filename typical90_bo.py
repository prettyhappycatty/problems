N, K = map(int, input().split())

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

#print(change8to10("0"))
#print(change10to9("0"))
if N == 0:
    print(0)
    exit()

tmp = N
for i in range(K):
    t = change8to10(str(tmp))
    #print("t",t)
    new_t = change10to9(str(t))
    #print("nt",new_t)
    str_t = str(new_t)
    tmp = str_t.replace("8","5")
    #print(tmp)

print(tmp)