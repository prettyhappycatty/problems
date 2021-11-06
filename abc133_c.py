L, R = map(int, input().split())

min_mul = 4*10**18
for i in range(L, R):
    for j in range(i+1, R+1):
        mul = (i*j) % 2019
        min_mul = min(min_mul, mul)
        if mul == 0:
            print(0)
            exit()

print(min_mul)
