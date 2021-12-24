N = int(input())
A = list(map(int, input().split()))

S = [0]
ss = 0
for i in range(N):
    ss += A[i]
    S.append(ss)

#print(S)

dic = {}
for i in range(len(S)):
    if S[i] not in dic.keys():
        dic[S[i]] = 0
    dic[S[i]] += 1

cnt = 0
for k, v in dic.items():
    if v > 1:
        for i in range(v, 1, -1):
            tmp = v*(v-1)//2
        cnt += tmp
print(cnt)