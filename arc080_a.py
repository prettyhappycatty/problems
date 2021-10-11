N = int(input())
A = list(map(int, input().split()))

mul = 1
for i in range(len(A)):
    if A[i] % 4 == 0:
        mul *= 4
    elif A[i] % 2 == 0:
        mul *= 2
    else:
        mul *= 1

#間の数
bet = N // 2
#print(mul,bet)
if mul >= 4**bet:
    print("Yes")
else:
    print("No")