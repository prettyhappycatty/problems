N = int(input())
A, B = {},{}
for i in range(N):
    tmpA, tmpB = map(int, input().split())
    A[i] = tmpA
    B[i] = tmpB
#print(A, B)
B_sort = sorted(B.items(), key=lambda x:x[1])
A_sort = sorted(A.items(), key=lambda x:x[1])

#print(A_sort, B_sort)
if A_sort[0][0] != B_sort[0][0]:
    print(max(A_sort[0][1], B_sort[0][1]))
else:
    print(min(max(A_sort[0][1],B_sort[1][1]), max(A_sort[1][1],B_sort[0][1]), A_sort[0][1]+B_sort[0][1]))