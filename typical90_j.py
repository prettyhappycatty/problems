N = int(input())

rui1_P = [0]
rui2_P = [0]

for i in range(N):
    tmp_C, tmp_P = map(int, input().split())
    if tmp_C == 1:
        rui1_P.append(rui1_P[i]+tmp_P)
        rui2_P.append(rui2_P[i])
    elif tmp_C == 2:
        rui1_P.append(rui1_P[i])
        rui2_P.append(rui2_P[i]+tmp_P)

#print(rui1_P,rui2_P)


Q = int(input())
for i in range(Q):
    tmp_L, tmp_R = map(int, input().split())
    print(rui1_P[tmp_R]-rui1_P[tmp_L-1], rui2_P[tmp_R]-rui2_P[tmp_L-1])
