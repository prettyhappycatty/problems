import copy

N, W = map(int, input().split())
#VV, WW = [],[]

dic = {}
for i in range(N):
    a, b = map(int, input().split())
    dic[i] = tuple((a,b))
#    VV.append(a)
#    WW.append(b)

dic_sorted = sorted(dic.items(), key=lambda x:x[1][0], reverse=True)
#print(dic_sorted)

rest = W
oishisa_sum = 0
for i in range(N):
    oishisa = dic_sorted[i][1][0]
    cheese = dic_sorted[i][1][1]

    if rest > cheese:
        oishisa_sum += oishisa*cheese
        #print("+",oishisa,cheese)
    else:
        oishisa_sum += oishisa*rest
        #print("+",oishisa,rest)
        break

    rest -= cheese
print(oishisa_sum)
