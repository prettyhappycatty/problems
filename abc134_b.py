N, D = map(int, input().split())

#print(D*2)
if N % (D*2+1) == 0:
    print(N // (D*2+1))
else:
    print(N // (D*2+1) + 1)