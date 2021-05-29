N = 15

A = []

for i in range(N):
    tmp_A = input()
    #print(tmp_A)
    A.append(tmp_A)
A.sort()
print(A[6])