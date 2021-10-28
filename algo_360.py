X = int(input())
A = list(map(int, input().split()))

mn = 10**8+8
for a0 in range(0, A[0]+1):
    for a1 in range(0,A[1]+1):
        for a2 in range(0,A[2]+1):
            if X - (a0*50 + a1*10 + a2 * 5) <= A[3] and X - (a0*50 + a1*10 + a2 * 5) >= 0:
                a3 = X - (a0*50 + a1*10 + a2 * 5)
                mn = min(mn,a0+a1+a2+a3)
				

print(mn)