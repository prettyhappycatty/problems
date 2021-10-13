N, K = map(int, input().split())

dic = {}

for i in range(N):
    a, b = map(int, input().split())
    if a not in dic.keys():
        dic[a] = 0
    dic[a] += b

#print(dic)

dic_sorted = sorted(dic.items(), key=lambda x:x[0])

print(dic_sorted)

dic_sum = 0
i = 0
while dic_sum <= K and i < len(dic_sorted)-1:
    dic_sum += dic_sorted[i][1]
    if dic_sum > K:
        break
    i = i + 1
    print(K, dic_sum)

print(i)
if i < len(dic_sorted):
    print(dic_sorted[i-1][0])

    