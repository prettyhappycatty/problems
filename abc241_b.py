N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dic_A = {}

for i in range(len(A)):
    if A[i] not in dic_A.keys():
        dic_A[A[i]] = 0
    dic_A[A[i]] += 1

for i in range(len(B)):
    if B[i] in dic_A.keys() and dic_A[B[i]] > 0:
        dic_A[B[i]] -= 1
    else:
        print("No")
        exit()

print("Yes")