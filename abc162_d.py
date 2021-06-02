#TLE

N = int(input())
S = input()

dic = {}

for i in range(N):
    if S[i] not in dic.keys():
        dic[S[i]] = []
    dic[S[i]].append(i)

#print(dic)

if "R" not in dic.keys() or  "G" not in dic.keys()  or "B" not in dic.keys() :
    print("0")
    exit()

cnt = 0
for k in dic["G"]:
    for l in dic["B"]:
        # 3パターン
        # j < k < l (kが真ん中)の場合、j != 2k-l  j-k != k-l
        # k < j < l (jが真ん中)の場合、j = (k + l)/2
        # j < l < k (lが真ん中)の場合、j = 2l - k j-l != l-k
        cnt += len(dic["R"])
        #print(dic["R"], 2*k-l, (k + l) % 2,2*l-k, l, k)
        if 2*k-l in dic["R"]:
            #print("minus")
            cnt -=1
        if (k + l)/2 in dic["R"]:
            #print("minus")
            cnt -=1
        if 2*l-k in dic["R"]:
            #print("minus")
            cnt -=1

print(cnt)
