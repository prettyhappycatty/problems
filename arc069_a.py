N, M = map(int, input().split())

ans = min(N, M//2)

if N*2 < M: #Sの個数の2倍よりもcの個数が多い場合
    c_rest = M - N*2
    ans += c_rest // 4
print(ans)