N, K = map(int, input().split())

A = list(map(int, input().split()))

def solve(x):
    #x <= (K-1)*n+1
    #x-1 <= (K-1)*n 
    #(x-1)/(K-1) <= n
    if (x-1) % (K-1) == 0: #割り切れるとき
        return (x-1) // (K-1)
    else:#割り切れないとき
        return (x-1) // (K-1) + 1

print(solve(N))