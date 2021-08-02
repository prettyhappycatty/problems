import heapq


Q = int(input())

hQ = []
A = []
S = []

tmpS = 0
for i in range(Q):
    tmp = list(map(int, input().split()))
    #print(len(hQ))
    if tmp[0] == 1:
        x = tmp[1]
        A.append(0)
        S.append(tmpS)
        heapq.heappush(hQ, x-tmpS)
    elif tmp[0] == 2: #最小値は変わらない
        x = tmp[1]
        tmpS += x
        S.append(tmpS)
        A.append(x)
    elif tmp[0] == 3:
        x = 0
        y = heapq.heappop(hQ)
        S.append(tmpS)
        A.append(0)
        #print("3",y)
        print(y+tmpS)

#print(A)
#print(S)