N = int(input())
A = {}
for i in range(N):
    tmp = int(input())
    if tmp not in A.keys():
        A[tmp] = 1
    else:
        A[tmp] += 1

A_sorted = list(sorted(A.items(), key=lambda x:x[0], reverse=True))
print(A_sorted[1][0])