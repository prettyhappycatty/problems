N, Q = map(int, input().split())

a = list(map(int, input().split()))
dic = {}

for i in range(N):
    if a[i] not in dic.keys():
        dic[a[i]] = []
    dic[a[i]].append(i+1)

#print(a)

for i in range(Q):
    x, k = map(int, input().split())
    if x not in dic.keys() or len(dic[x]) < k:
        print(-1)
    else:
        print(dic[x][k-1])

