N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
i, j = 0, 0
ans = []
#print(A, B)
while i < N or j < M:
#    print(i,j)
    if i == N:
#        print(1)
        ans.extend(B[j:])
        j = M
    elif j == M:
#        print(2)
        ans.extend(A[i:])
        i = N
    else:
#        print(3)
        if A[i] < B[j]:
            ans.append(A[i])
            i += 1
        elif A[i] > B[j]:
            ans.append(B[j])
            j += 1
        else:
            i += 1
            j += 1

print(*ans)