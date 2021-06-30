N, K = map(int, input().split())

dic = {}

for i in range(N):
    tmpA, tmpB = map(int, input().split())
    #label1 = str(i) + "-A"
    label2 = str(i) + "-B"
    label3 = str(i) + "-AB"
    #dic[label1] = tmpA 
    dic[label2] = tmpB
    dic[label3] = tmpA - tmpB 

dic_sorted = sorted(dic.items(), key=lambda x:x[1], reverse=True)

#print(dic_sorted)

i = 0
su = 0
dic2 = {}
for j in range(len(dic_sorted)):
    k = dic_sorted[j][0]
    #print(k)
    #print(dic_sorted[j][1])
    if i < K:
        if "-B" in k:
            i += 1
            su += dic_sorted[j][1]
            dic2[k] = True
        elif "-AB" in k:
            tmp = k.replace("-AB", "") + "-B"
            if tmp in dic2.keys():
                i += 1
                su += dic_sorted[j][1]
                dic2[k] = True

print(su)
