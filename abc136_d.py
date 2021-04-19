S = input()

#文字数より多い偶数回操作をする
bef = S[0]
cnt = 1
ary = [] #LRのセットに分ける
newstr = S[0]
for i in range(1, len(S)):
    if bef == 'L' and S[i]=='R':
        ary.append(newstr)
        newstr = 'R'
    else:
        newstr += S[i]
    bef = S[i]
ary.append(newstr)
#print(ary)

def retPlc(st):
    bef = st[0]
    num = {i:0 for i in range(len(st))}
    for i in range(len(st)):
        if bef == 'R' and st[i]== 'L':#最終位置候補
            last1 = i-1
            last2 = i
            #print(last1, last2)
        bef = st[i]

    for i in range(len(st)):
        if (i - last1) % 2 == 0:#ぐうきが同じ時
            num[last1] += 1
        else:
            num[last2] += 1

    return num

ansary = []

for i in range(len(ary)):
    newdic = retPlc(ary[i])
    #print(newdic)
    for i, j in newdic.items():
        ansary.append(j)

print(*ansary)