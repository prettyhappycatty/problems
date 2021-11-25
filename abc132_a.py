S = input()
dic = {}
for i in range(len(S)):
    if S[i] not in dic.keys():
        dic[S[i]] = 0
    dic[S[i]] += 1

if len(dic) == 2:
    lst = list(dic.values())
    if lst[0] == lst[1]:
        print("Yes")
    else:
        print("No")
else:
    print("No")