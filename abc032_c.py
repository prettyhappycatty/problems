N, K = map(int, input().split())

S =[]
for i in range(N):
    S.append(int(input()))

if 0 in S:
    print(N)
    exit()

i = 0
j = 0
ml = 1
maxl = 0
while i < N and j < N:
    if i > j:
        j = i
    #print(ml)
    if ml*S[j] <= K:
        maxl = max(maxl, j-i+1)
        #print(i,j,ml,K,S[j],maxl)
        ml *= S[j]
        j += 1
    elif j > i:
        ml //= S[i]
        i += 1
    else:
        i += 1
    
print(maxl)