A,B  = list(map(int,input().split()))

aryA = []
sum_A = 0
sum_B = 0

if A == B:
    for i in range(A):
        aryA.append(i+1)
        sum_A += i
        aryA.append(-i-1)
        sum_B -= i
else:
    for i in range(A):
        aryA.append((i+1)*B)
        sum_A += (i+1)*B
    #print(aryA[A-1], sum_A)
    for i in range(B):
        aryA.append(-(i+1)*A)
        sum_B += -(i+1)*A
    #print(aryA[A+B-1], sum_B)
    if abs(sum_A) - abs(sum_B) > 0:
        aryA[A+B-1] = aryA[A+B-1] - (abs(sum_A) - abs(sum_B))
    else:
        aryA[A-1] = aryA[A-1] + (abs(sum_B) - abs(sum_A))



#print(aryA, sum_A,sum_B)
print(*aryA)

