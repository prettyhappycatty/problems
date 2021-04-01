N = int(input())
L = []

L.append(2)
L.append(1)

#print(L)
#print(L[0], L[1])

for i in range(2, N+2):
    #print(i)
    L_tmp = L[i-2] + L[i-1]
    #print(L_tmp)
    L.append(L_tmp)

print(L[N])
