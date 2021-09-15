N, M = map(int, input().split())

ary = []

for i in range(M):
    ary.append(tuple(map(int, input().split())))

ary2 = sorted(ary, key=lambda x:x[1])
ary2 = sorted(ary2, key=lambda x:x[0])
#print(ary)

bef_pref = 0
bef_city = 0
cnt_pref = 0
cnt_city = 0
dic = {}
for a in ary2:
    pref = a[0]
    city = a[1]
    if pref == bef_pref:#県が同じならcityを増やす
        cnt_city += 1
    else:
        cnt_pref += 1
        cnt_city = 1
    bef_city = city
    bef_pref = pref
    dic[(pref, city)] = "0"*(6-len(str(pref))) + str(pref)+"0"*(6-len(str(cnt_city))) + str(cnt_city)

for a in ary:
    pref = a[0]
    city = a[1]
    print(dic[(pref, city)])