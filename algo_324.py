A = list(map(int, input().split()))

AA = [A]

bef = AA[0]
for i in range(4):
    ar = []
    for j in range(4):
        if j < 1:
            left = 0
            center = bef[j]
            right = bef[j+1]
        elif j < 3:
            left = bef[j-1]
            center = bef[j]
            right = bef[j+1]
        else:
            left = bef[j-1]
            center = bef[j]
            right = 0
        ar.append(left+center+right)
    AA.append(ar)
    bef = ar
#print(AA)
print(AA[i][j])