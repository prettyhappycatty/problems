#いもす法

N, W = map(int, input().split())

dic = {}
for i in range(N):
    S, T, P = map(int, input().split())
    if S not in dic.keys():
        dic[S] = 0
    if T not in dic.keys():
        dic[T] = 0
    dic[S] += P
    dic[T] -= P

dic_sorted = list(sorted(dic.items(), key=lambda x:x[0]))

max_water = [0]
max_w = 0
for i in range(len(dic_sorted)):
    t = dic_sorted[i][0]
    p = dic_sorted[i][1]
    max_water.append(max_water[i]+p)
    max_w=max(max_w, max_water[i]+p)

if max_w <= W:
    print("Yes")
else:
    print("No")
