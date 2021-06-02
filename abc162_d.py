#TLE

N = int(input())
S = input()

dic = {}

for i in range(N):
    if S[i] not in dic.keys():
        dic[S[i]] = []
    dic[S[i]].append(i)

if "R" not in dic.keys() or  "G" not in dic.keys()  or "B" not in dic.keys() :
    print("0")
    exit()

cnt = len(dic["R"])*len(dic["G"])*len(dic["B"])

for i in range(N):
    for j in range(i+1, N):
        k = j + (j-i)
        if N > k and S[i] != S[j] and S[i] != S[k] and S[k] != S[j]:
            #print("minus")
            cnt -=1

print(cnt)
