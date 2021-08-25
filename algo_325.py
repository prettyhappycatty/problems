N = int(input())
A = list(map(int, input().split()))

AA = [A]

bef = AA[0]
for i in range(N):
    ar = []
    for j in range(N):
        if j < 1:
            left = 0
            center = bef[j]
            right = bef[j+1]
        elif j < N-1:
            left = bef[j-1]
            center = bef[j]
            right = bef[j+1]
        else:
            left = bef[j-1]
            center = bef[j]
            right = 0
        ar.append((left+center+right)%100)
    AA.append(ar)
    bef = ar
#print(AA)
print(AA[i][j])