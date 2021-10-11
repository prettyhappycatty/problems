N = int(input())

def func(n):
    if n < 2:
        return 1
    return n*func(n-2)


if N % 2 == 1:
    print(0)
    exit()

ans = N // 10 #10個数
N //= 10

prime5 = 5
while prime5 <= N:
    ans += N // prime5
    prime5 *= 5

print(ans)

