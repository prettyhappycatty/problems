N, K = list(map(int, input().split()))

#N>Kの時いきなり終わるかも

sum_ratio = 0
for i in range(1, N+1):
    #最初の目で回す
    cnt = i
    
    #print("first",cnt)
    ratio = 1 / N
    while cnt < K:
        cnt *= 2
        #print(cnt)
        ratio /= 2
    sum_ratio += ratio
    #print(ratio)

print(sum_ratio)