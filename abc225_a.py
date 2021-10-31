S = input()

dic = {}

for i in range(len(S)):
    if S[i] not in dic.keys():
        dic[S[i]] = 0
    dic[S[i]] += 1

if len(list(dic)) == 1:
    print(1)
elif len(list(dic)) == 2:
    print(3)
else:
    print(6)