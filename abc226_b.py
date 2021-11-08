N = int(input())

dic = {}

for i in range(N):
    l = list(map(int, input().split()))
    tp = tuple((l[1:]))
    if tp not in dic.keys():
        dic[tp] = 0
    dic[tp] += 1

print(len(list(dic)))
