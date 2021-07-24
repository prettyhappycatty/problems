S = input()
N = len(S)

rS = "chokudai"
DP = [[0 for _ in range(9)] for _ in range(len(S)+1)]

M = 1000000007
DP[0][0] = 1
for i in range(len(S)):
    for j in range(9):
        #print(i,j)
        DP[i + 1][j] += DP[i][j]
        if S[i] == 'c' and j == 0:DP[i + 1][j + 1] += DP[i][j]
        if S[i] == 'h' and j == 1:DP[i + 1][j + 1] += DP[i][j]
        if S[i] == 'o' and j == 2:DP[i + 1][j + 1] += DP[i][j]
        if S[i] == 'k' and j == 3:DP[i + 1][j + 1] += DP[i][j]
        if S[i] == 'u' and j == 4:DP[i + 1][j + 1] += DP[i][j]
        if S[i] == 'd' and j == 5:DP[i + 1][j + 1] += DP[i][j]
        if S[i] == 'a' and j == 6:DP[i + 1][j + 1] += DP[i][j]
        if S[i] == 'i' and j == 7:DP[i + 1][j + 1] += DP[i][j]
		
    for j in range(9):
        DP[i + 1][j] %= M

#print(DP)

print(DP[len(S)][8] % (10**9+7))
