N = int(input())
A = list(map(int, input().split()))

dic = {}
cnt = 0

for i in range(N):
    rest = A[i] % 200
    if rest not in dic.keys():
        dic[rest] = 0
    dic[rest] += 1
#print(dic)

for key, value in dic.items():
    cnt += value*(value-1)/2

print(int(cnt))