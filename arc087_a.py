N = int(input())
A = list(map(int, input().split()))

dic = {}

for i in range(N):
    if A[i] not in dic.keys():
        dic[A[i]] = 0
    dic[A[i]] += 1

#print(dic)

cnt = 0
for k,v in dic.items():
    if k > v:
        #print(k,v)
        cnt += v
    elif k < v:
        #print(k,v-k)
        cnt += v-k

print(cnt)
