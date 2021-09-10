N = int(input())

# A * B + C = Nのとき
# Aを固定すると、BはN-1//A個ある

cnt = 0
for A in range(1, N):
    B = (N-1) // A
    cnt += B

print(cnt)