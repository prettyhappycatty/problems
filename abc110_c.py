S = input()
T = input()

dic = {}
dicT = {}

for i in range(len(S)):
    if S[i] not in dic.keys():
        dic[S[i]] = T[i]
    if T[i] not in dicT.keys():
        dicT[T[i]] = S[i]
    if S[i] in dic.keys():
        if dic[S[i]] != T[i]:
            print("No")
            exit()
    if T[i] in dic.keys():
        if dicT[T[i]] != S[i]:
            print("No")
            exit()
print("Yes")