S = list(input())
N = int(input())
for i in range(N):
    tmpL, tmpR = map(int, input().split())
    tmpL -= 1
    #tmpR -= 1
    newS = []
    for j in range(0, tmpL):
        newS.append(S[j])
    for j in range(tmpL, tmpR):
        idx = tmpR-(j-tmpL)-1
        #print(idx)
        newS.append(S[idx])
    for j in range(tmpR, len(S)):
        newS.append(S[j])
    #print(tmpL, tmpR, newS)
    S = newS

ans = ""
for i in range(len(S)):
    ans += S[i]
print(ans)
