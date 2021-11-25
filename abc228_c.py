N, K = map(int, input().split())
P = []
sumP = {}
inai = {i:False for i in range(N)}
for i in range(N):
    tmpP = list(map(int, input().split()))
    P.append(tmpP)
    sumP[i] = sum(tmpP)

#print(P)
sumP_sorted = sorted(sumP.items(), key=lambda x:x[1], reverse=True)
#print(sumP_sorted)
#print(sumP_sorted[K-1])
#print(sumP_sorted[K])
border = sumP_sorted[K-1][1]-300
for i in range(len(sumP_sorted)):
    who = sumP_sorted[i][0]
    point = sumP_sorted[i][1]
    if point < border:
        inai[who] = True

for i in range(len(inai)):
    if inai[i]:
        print("No")
    else:
        print("Yes")




