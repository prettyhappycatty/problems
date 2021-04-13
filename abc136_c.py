N = int(input())
H = list(map(int, input().split()))

chk = 0
for i in range(N-1):
    if H[i] < H[i+1]:
        H[i+1] -= 1

    if H[i] > H[i+1]:
        chk = 1
        break

#print(H, chk)

if N == 1 or chk == 0:
    print('Yes')
else:
    print('No')


