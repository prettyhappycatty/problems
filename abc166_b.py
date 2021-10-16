N, K = map(int, input().split())

sweets = {i:0 for i in range(N)}

for i in range(K):
    d = int(input())
    tmpA = list(map(int, input().split()))
    for j in range(d):
        sweets[tmpA[j]-1] += 1

cnt = 0
#print(sweets)
for l in range(len(sweets)):
    if sweets[l] == 0:
        cnt +=1

print(cnt)


