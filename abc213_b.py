N = int(input())

A = list(map(int, input().split()))

fst = 0
fst_id = -1
scd = 0
scd_id = -1
for i in range(len(A)):
    if fst == 0:#最初の時
        fst = A[i] 
        fst_id = i
    elif fst > 0 and scd == 0 and fst >= A[i] :#2番目が最初より大きいの時
        scd = A[i]
        scd_id = i
    elif fst > 0 and scd == 0 and scd < A[i]:#2番目が最初より小さいの時
        scd = fst
        scd_id = fst_id
        fst = A[i]
        fst_id = i
    elif A[i] >= fst:
        scd = fst
        scd_id = fst_id
        fst = A[i]
        fst_id = i
    elif fst > A[i] >= scd:
        scd_id = i
        scd = A[i]

print(scd_id+1)
    