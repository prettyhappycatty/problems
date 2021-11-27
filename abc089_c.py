# March

#5
#MASHIKE
#RUMOI
#OBIRA
#HABORO
#HOROKANAI

N = int(input())
march = "MARCH"

dic = {march[i]:0 for i in range(5)}
for i in range(N):
    tmp = input()
    if tmp[0] not in dic.keys():
        dic[tmp[0]] = 0
    dic[tmp[0]] += 1

#print(dic)


ans = 0
for i in range(5):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
#            print(dic[march[i]],dic[march[j]],dic[march[k]])
            ans += dic[march[i]]*dic[march[j]]*dic[march[k]]
print(ans)