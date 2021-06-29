#隣接リストを作る

N = int(input())

dic = {}
# dic[1] = [2, 3]

for i in range(N):
    tmpA, tmpB = map(int, input().split())
    if tmpA not in dic.keys():
        dic[tmpA] = []
    if tmpB not in dic.keys():
        dic[tmpB] = []
    dic[tmpB].append(tmpA)
    dic[tmpA].append(tmpB)

print(dic)

