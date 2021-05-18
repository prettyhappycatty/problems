N =  int(input())

A = list(map(int, input().split()))

bef = A[0]
cut = 0
bef_type = -1
for i in range(0, N-1):
    if A[i] < A[i+1]:
        diff_type = 0
    elif A[i] > A[i+1]:
        diff_type = 1
    else:
        diff_type = bef_type #ステイの場合は変えない

    #print(diff_type, bef_type)
    if bef_type > -1 and bef_type != diff_type:
        cut += 1
        #print("cut")
        diff_type = -1
    bef_type = diff_type
print(cut+1)


