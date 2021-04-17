A, B, C = list(map(int, input().split()))

max_3 = max(A, B, C)

if max_3 % 2 == 1:
    print(A*B*C//max_3)
else:
    print(0)