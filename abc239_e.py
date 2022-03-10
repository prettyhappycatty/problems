import heapq

N, Q = map(int, input().split())
X = list(map(int, input().split()))
A = []
B = []
G = {i:[] for i in range(N)}
dept = [-1 for i in range(N)]
dept[0] = 0
x_list = [[-X[i]] for i in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    if dept[a-1] > -1:#すでに深さが決まっている時
        A.append(a-1)
        G[a-1].append(b-1)
        x_list[a-1].append(-X[b-1])
        dept[b-1] = dept[a-1]+1
    elif dept[b-1] > -1:#すでに深さが決まっている時
        B.append(b-1)
        G[b-1].append(a-1)
        x_list[b-1].append(-X[a-1])
        dept[a-1] = dept[b-1]+1

V = []
K = []


#print(A,B,V,K,G)
#print(x_list)

def dfs(i):
    if len(G[i])==0:
        return []
    else:
        retary = x_list[i]
        for j in G[i]:
            retary = list(heapq.merge(retary,dfs(j)))
            heapq.heapify(retary)
        x_list[i] = retary
        return retary

dfs(0)

for i in range(len(x_list)):
    print(x_list[i])
#    while x_list[i]:
#        q = heapq.heappop(x_list[i])
#        print(i, -q)


for i in range(Q):
    v, k = map(int, input().split())
    #V.append(v-1)
    for j in range(k):
        p = heapq.heappop(x_list[v-1])
#        print(j,-p)
    print(-p)
    
    #K.append(k)