#隣接リストを作る

N, M = map(int, input().split())

dic = {}
# dic[1] = [2, 3]

for i in range(M):
    tmpA, tmpB = map(int, input().split())
    if tmpA not in dic.keys():
        dic[tmpA] = []
    if tmpB not in dic.keys():
        dic[tmpB] = []
    dic[tmpB].append(tmpA)
    dic[tmpA].append(tmpB)

#print(dic)

cnt = 0
for k in dic.keys():
    tmp_cnt = 0
    for v in dic[k]:
        if v < k:
            tmp_cnt += 1
        if tmp_cnt > 1:
            break
    if tmp_cnt == 1:
        cnt += 1
print(cnt)
