# 3 step
#   1. subproblem
#       dp[i][j]:i回目にjとなるかどうか、True/False
#       dp[0][2] = True
#       dp[1][2-1] = dp[1][2-1] or (dp[0][2] and 2-1 != NG)
#       dp[1][2-2] = dp[1][2-2] or (dp[0][2] and 2-1 != NG)
#       dp[1][2-1] = dp[1][2-1] or (dp[0][2] and 2-1 != NG)
#   2. recurence elations
#       dp[i][j] = dp[i-1][j-1] or dp[i-2][j-2] or dp[i-3][j-3]
#
#   3. base case
#       dp[0][N] = True
#       othe = False

N = int(input())
NG1 = int(input())
NG2 = int(input())
NG3 = int(input())

dp = []
for i in range(101):
    tmp_dp = []
    for j in range(N+1):
        tmp_dp.append(False)
    dp.append(tmp_dp)

dp[0][N] = True

def isOK(a):
    if NG1 == a or NG2 == a or NG3 == a:
        return False
    return True 

if isOK(N) == False:
    print("NO")
    exit()
    

for i in range(100):
    for j in range(N, -1, -1):
#       dp[1][N-1] = dp[1][N-1] or (dp[0][N-1] or N-1 != NG)
        #print(i+1, j)
        #print(dp[i][j-1], dp[i][j-2], dp[i][j-3], isOK(j-3), (dp[i][j] & isOK(j-3)))
        if j >= 3:
            dp[i+1][j-3] = dp[i+1][j-3] or (dp[i][j] & isOK(j-3))
        if j >= 2:
            dp[i+1][j-2] = dp[i+1][j-2] or (dp[i][j] & isOK(j-2))
        if j >= 1:
            #print(i, j, i+1, j-1)
            dp[i+1][j-1] = dp[i+1][j-1] or (dp[i][j] & isOK(j-1))
        #print(dp[i+1][j-1], dp[i+1][j-2], dp[i+1][j], isOK(j-3), dp[i+1][0])
        if dp[i+1][0] == True:
            print("YES")
            exit()

print("NO")