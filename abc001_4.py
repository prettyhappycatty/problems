N = int(input())

T = []

def getTimeBlock(t):
    h = t // 100
    m = (t % 100) // 5
    return h*12 + m

for i in range(N):
    s = input()
    s_sep = list(map(int, s.split("-")))
    st = getTimeBlock(s_sep[0])
    if s_sep[1] % 100 == 0:
        h = s_sep[1] // 100 -1
        m = 59
    else:
        h = s_sep[1] // 100
        m = s_sep[1] % 100 - 1
    en = getTimeBlock(h*100+m)
    T.append(tuple((st, en)))
    #print(st, en)

T.sort(key=lambda x:x[0])

#print(T)

bef = T[0]
ans = []
for i in range(1, len(T)):
    if bef[1] + 1 >= T[i][0]: #連続するとき
        bef = tuple((bef[0], max(T[i][1], bef[1])))
    else:
        ans.append(bef)
        bef = T[i]
ans.append(bef)

#print(ans)

def cntToTime(bef, aft):
    bef_h = bef // 12
    bef_m = (bef % 12) * 5
    aft_h = aft // 12
    aft_m = (aft % 12) * 5 + 5
    if aft_m == 60:
        aft_h += 1
        aft_m = 0
    b = str(bef_h*100+bef_m)
    a = str(aft_h*100+aft_m)

    return "0"*(4-len(b)) + b + "-" + "0"*(4-len(a))  + a

for i in range(len(ans)):
    print(cntToTime(ans[i][0],ans[i][1]))