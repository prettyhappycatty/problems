H, W, N = map(int, input().split())

H_tmp = {}
W_tmp = {}

A = []
B = []

for i in range(N):
    tmpA, tmpB = map(int,input().split())
    A.append(tmpA)
    B.append(tmpB)
    if tmpA not in H_tmp.keys():
        H_tmp[tmpA] = []
    H_tmp[tmpA].append(tmpB)
    W_tmp[tmpB] = True

H_sorted = sorted(H_tmp.items(), key=lambda x:x[0])
W_sorted = sorted(W_tmp.items(), key=lambda x:x[0])

H_map = {}
W_map = {}

for i in range(len(H_sorted)):
    H_map[H_sorted[i][0]] = i+1

for i in range(len(W_sorted)):
    W_map[W_sorted[i][0]] = i+1

for i in range(len(A)):
    print(H_map[A[i]], W_map[B[i]])

#print(H_map, W_map)