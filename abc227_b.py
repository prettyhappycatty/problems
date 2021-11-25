N = int(input())

S = list(map(int, input().split()))
dic = {}#S[i]と予想した人数を管理

for i in range(N):
    if S[i] not in dic.keys():
        dic[S[i]] = 0
    dic[S[i]] += 1

#print(dic)
for a in range(1,1000):
    for b in range(1,1000):
        k = 4*a*b + 3*a + 3*b
        if k in dic.keys():
            #print(a,b,k)
            dic[k] = 0

#print(dic)

cnt = 0
for k,v in dic.items():
    cnt += v

print(cnt)