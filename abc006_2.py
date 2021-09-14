# フィボナッチじゃなくてトリボナッチ数列

N = int(input())
#N = 100

MOD = 10**4+7

T = [0, 0, 1]

for i in range(2, N):
    T.append((T[i-2]+T[i-1]+T[i]) % MOD)

print(T[N-1])