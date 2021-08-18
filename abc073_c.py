N = int(input())

dic = {}

for i in range(N):
    tmp = int(input())
    if tmp not in dic.keys():
        dic[tmp] = 0

    dic[tmp] += 1

#print(dic)
cnt = 0
for s in dic.keys():
    if dic[s] % 2 != 0:
        cnt += 1

print(cnt)
