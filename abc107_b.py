H, W = list(map(int, input().split()))

ary = []

for i in range(H):
    tmp = input()

    if '#' in tmp:
        ary.append(tmp)

ary2 = []

for j in range(W):
    flg = 0
    for i in range(len(ary)):
        if ary[i][j] != '.':
            flg = 1
    if flg == 1:
        ary2.append(j)

#print(ary2)

for i in range(len(ary)):
    line = ''
    for j in range(W):
        if j in ary2:
            line += ary[i][j]
    print(line)

