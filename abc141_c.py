N, K, Q = list(map(int, input().split()))
acc = {}
for i in range(1, N+1):
    acc[i] = 0

for i in range(Q):
    tmp = int(input())
    acc[tmp] += 1

#print(acc, Q)

for i in range(1, N+1):
    lose = Q-acc[i]
    if K - lose > 0:
        print('Yes') 
    else:
        print('No')
