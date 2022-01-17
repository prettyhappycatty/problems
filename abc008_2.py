N = int(input())

dic = {}

for i in range(N):
    S = input()
    if S not in dic.keys():
        dic[S] = 0
    dic[S] += 1

#print(dic)

dic_sorted = sorted(dic.items(), key=lambda x:x[1], reverse=True)
print(dic_sorted[0][0])