N = int(input())
A = list(map(int, input().split()))

dic = {}

for i in range(N):
    if A[i] not in dic.keys():#初めて出てくる数字の場合
        dic[A[i]] = 1
    else:
        dic[A[i]] += 1

cnt = 0
for k,v in dic.items():
    cnt += v*(v-1)//2

print(N*(N-1)//2-cnt)
