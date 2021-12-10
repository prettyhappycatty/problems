N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

def q2(i,j):
    if abs(i - A) == abs(j - B):
        return True
    else:
        return False    

for i in range(P, Q+1):
    tmp_mat = []
    for j in range(R, S+1):
        if q2(i,j):
            tmp_mat.append("#")
        else:
            tmp_mat.append(".")
    print(''.join(tmp_mat))
