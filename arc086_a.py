N, K = map(int, input().split())

A= list(map(int, input().split()))

dic = {}

for i in range(N):
    if A[i] not in dic.keys():
        dic[A[i]] = 0
    dic[A[i]] += 1

dic_sorted = sorted(dic.items(), key=lambda x:x[1], reverse=False)

len_sorted = len(list(dic_sorted))
lst_sorted = list(dic_sorted)
#print(lst_sorted)
if  len_sorted<= K:
    print(0)
else:
    sum_change = 0
    for j in range(len_sorted - K):
        sum_change += dic_sorted[j][1]
    print(sum_change)

#print(dic_sorted)