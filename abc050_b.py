N = int(input())
T = list(map(int, input().split()))

M = int(input())
P = []
X = []
for i in range(M):
    P_tmp, X_tmp = list(map(int, input().split()))
    P.append(P_tmp)
    X.append(X_tmp)

#print(P)
#print(T)
#print(X)
for i in range(M):#drink loop
    i_idx = i
    sum_T = 0
    #print('drink:',i_idx)
    for j in range(N): #problem loop
        j_idx = j
        p_idx = P[i_idx]-1
        #print('problem:',j_idx, ' shortcut:', T[j_idx])
        #print(i_idx, j_idx, p_idx, T[j_idx], X[i_idx])
        if p_idx == j_idx:
            sum_T += X[i_idx]
        else:
            sum_T +=  T[j_idx]
    print(sum_T)
