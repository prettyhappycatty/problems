N = int(input())
A = list(map(int, input().split()))

B = []

mul = 1
mul_odd = 1
for i in range(N):
    #if A[i] == 1:
    #    tmp = (A[i], A[i]+1)
    #    mul_odd *= 1
    #    mul *= 2
    #elif A[i] == 100:
    #    tmp = (A[i]-1, A[i])
    #    mul_odd *= 1
    #    mul *= 2
    #else:
    #    tmp = (A[i]-1, A[i], A[i]+1)
    #    mul *= 3
    #    if (A[i] % 2 == 0):
    #        mul_odd *= 2
    #    else:
    #        mul_odd *= 1
    tmp = (A[i]-1, A[i], A[i]+1)
    mul *= 3
    if (A[i] % 2 == 0):
       mul_odd *= 2
    else:
       mul_odd *= 1

    B.append(tmp)

print(mul-mul_odd)