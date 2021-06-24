from copy import copy

N = int(input())

if N % 2 == 1:
    print("")
    exit()

ary = ["0","1"]

#bit全探索用データ作り
for j in range(N-1):
    ary2 = copy(ary)
    for i in range(len(ary)):
        ary[i] = "0" + ary[i] 
        ary2[i] = "1" + ary2[i]
    ary.extend(ary2)

#print(ary)



#print(a_set)
                    
for s in ary:
    #print(s)
    sum0 = 0
    sum1 = 0
    for i in range(len(s)):
        if s[i] == "1":
            sum1 += 1
        else:
            sum0 += 1
        #print(s[i], sum0, sum1)
        if sum0 < sum1:
            break 

    #print(sum0, sum1)
    if sum0 == sum1:
        s_ans = s.replace("0","(").replace("1",")")
        print(s_ans)


