N, M = map(int, input().split())

B = []

def check(b_list, start):
    if start != b_list[0]:
        return False

    mod0_i = -1
    for i in range(len(b_list)):
        if b_list[i] != start + i:
            return False
        if b_list[i] % 7 == 0:
            mod0_i = i
    
    if mod0_i > -1 and mod0_i < len(b_list)-1:
        return False
    return True

for i in range(N):
    b_tmp = list(map(int, input().split()))
    if i == 0:
        b_start = b_tmp[0]
    else:
        b_start = b_start + 7

    ans = check(b_tmp, b_start)
    if ans == False:
        print("No")
        exit()

    #B.append(b_tmp)

print("Yes")

#iが1増えると、Bは7増える B[i+1][j] = B[i][j]+7
#jが1増えると、Bも1増える B[i][j+1] = B[i][j]+1 ただし、7,8みたく、7で割った時のあまりがB[i][j]のとき0の場合には、B[i][j+1]が存在してはいけない
