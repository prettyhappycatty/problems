
R, C, K = map(int, input().split())
s = []

for i in range(R):
    s.append(list(input()))

rui = [[0] for i in range(R)]
for i in range(R):
    for j in range(C):
        if s[i][j] == "x":
            rui[i].append(rui[i][j]+1)
        else:
            rui[i].append(rui[i][j])
            
ans = 0
for ri in range(K-1,R-K+1):
    for ci in range(K-1,C-K+1):
        for i in range(1,K):
            if rui[ri-i][ci+K-i]!=rui[ri-i][ci-K+1+i]:
                break
            if rui[ri+i][ci+K-i]!=rui[ri+i][ci-K+1+i]:
                break
        else:
            if rui[ri][ci+K]==rui[ri][ci-K+1]:
                ans+=1
                #print(ri,ci)
print(ans)

