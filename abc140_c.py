N = int(input())
B = list(map(int,input().split()))
A = []

A.append(B[0])
cnt = B[0]
for i in range(N-2):
    #print(i)
    if B[i] > B[i+1]:
        A.append(B[i+1])
        cnt += B[i+1]
    else:
        A.append(B[i])
        cnt += B[i]

A.append(B[N-2])
cnt += B[N-2]
print(cnt)

