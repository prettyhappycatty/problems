N = int(input())
S = []
for i in range(N):
    s = list(input())
    S.append(s)

#print(S)

#neigh_set = ()

def check(ii,jj):
    if ii + 5 >= N or jj + 5 >= N:
        return False
    check_i = [0, 0, 0, 0, 0, 0]#横列の個数
    check_j = [0, 0, 0, 0, 0, 0]#縦列の個数
    check_ij = [0, 0]#斜め
    for i in range(6):
        for j in range(6):
            if S[ii+i][jj+j] == "#":
                check_i[i] += 1

    for j in range(6):
        for i in range(6):
            if S[ii+i][jj+j] == "#":
                check_j[j] += 1
    
    for k in range(6):
        if S[ii+k][jj+k] == "#":
            check_ij[0] += 1
        if S[ii+5-k][jj+k] == "#":
            check_ij[1] += 1
            
    if 4 in check_i or 5 in check_i or 6 in check_i:
        return True
    if 4 in check_j or 5 in check_j or 6 in check_j:
        return True
    if 4 in check_ij or 5 in check_ij or 6 in check_ij:
        return True
    return False

for i in range(N):
    for j in range(N):
        if check(i,j) == True:
            print("Yes")
            exit()
print("No")

