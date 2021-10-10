N, M = map(int, input().split())

A = []
win = { i: 0 for i in range(2*N) } # 0-index, -1スル　#回数
for i in range(2*N):
    tmpA = input()
    A.append(tmpA)

#print(A)

def which_win(i1, s1, i2, s2):#あいこの場合は-1
    if (s1 == "G" and s2 == "P") or  (s1 == "P" and s2 == "C") or (s1 == "C" and s2 == "G"):
        return i2
    if (s1 == "P" and s2 == "G") or  (s1 == "C" and s2 == "P") or (s1 == "G" and s2 == "C"):
        return i1
    return -1

win_sorted = sorted(win.items(), key=lambda x:x[0])
#print(win_sorted)
for i in range(M):#M回対戦
    for j in range(N):#N個の組み合わせ
        who1 = win_sorted[2*j][0]
        who2 = win_sorted[2*j+1][0]
        what1 = A[who1][i]
        what2 = A[who2][i]
        #print(who1, who2, what1, what2)
        who_win = which_win(who1, what1, who2, what2)
        #print(who_win)
        if who_win > -1:
            win[who_win] += 1
        win_sorted = sorted(win.items(), key=lambda x:x[1], reverse=True)

for it in win_sorted:
    print(it[0]+1)
    
        
    