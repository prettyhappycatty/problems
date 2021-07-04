import copy

N, K = map(int, input().split())

A = list(map(int, input().split()))
B = copy.deepcopy(A)

A.sort()

#rint(A)
ans = K // N
rest = K % N

border = A[rest]
#boderより小さい番号の人のみ＋１
#print(border)

for i in range(N):
    if B[i] < border:
        print(ans+1)
    else:
        print(ans)


