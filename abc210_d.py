H, W, C = map(int, input().split())

A = []
for i in range(H):
    tmpA = list(map(int, input().split()))
    A.append(tmpA)

# 線路の建設費用を出すための配列
smallestA_i = 0 
smallestA_j = 0 
smallestA = 10**9 
for i in range(H):
    for j in range(W):
        if A[i][j] < smallestA:
            smallestA_i = i 
            smallestA_j = j
            smallestA = A[i][j]


smallest_i = []
smallest_j = []

for i in range(H):
    for j in range(W):
        if A[i][j] == smallestA:
            smallest_i.append(i)
            smallest_j.append(j)

#print(smallestA) 

def check(smi, smj):

    m = [[-1 for _ in range(W)]  for _ in range(H)]
    m[smi][smj] = 0

    #print(m)

    smallest_cost = 10**9 * C
    for i in range(H):
        for j in range(W):
            if smi == i and smj == j:
                continue
            else:
                cost = C*(abs(smj-j)+abs(smi-i))+A[i][j]
                m[i][j] = cost
                if cost < smallest_cost:
                    #print(i,j)
                    smallest_cost = cost

    return smallest_cost+smallestA


real_smallest = 10 ** 9 * C
for k in range(len(smallest_i)):
    #print((smallest_i[k], smallest_j[k]))
    rs = check(smallest_i[k], smallest_j[k])
    if real_smallest < rs:
        rs = real_smallest

print(rs)