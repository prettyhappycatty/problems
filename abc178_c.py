# 包除原理
# ans = 10**N - 9**N - 9**N - 8**N
# pow mod mod_pow pow_mod

MOD = 10**9 + 7

def pow_mod(n, m):
    ret = 1
    for _ in range(m):
        ret *= n
        ret %= MOD
    
    return ret

N = int(input())
pow10 = pow_mod(10, N)
pow9 = pow_mod(9,N)
pow8 = pow_mod(8, N)

print((pow10 - 2*pow9 + pow8) % MOD)