N = int(input())
S = input()

rS = "atcoder"
DP = [[0 for _ in range(N+1)] for _ in range(8)]

#print(DP)
#print("a  t  t  c  o  r  d  e  e  r")
#print(S)
DP[0][0] = 1
for i in range(len(S)):#"Sの何文字目まで"
    for j in range(7): #"atcoderの何文字目まで"
        #print(S[i], rS[j],DP[j+1][i+1],DP[j][i])
        DP[j][i+1] += DP[j][i]
        if (S[j] == 'a' and j == 0) :DP[j + 1][i + 1] += DP[i][j]
        if (S[j] == 't' and j == 1) :DP[j + 1][i + 1] += DP[i][j]
        if (S[j] == 'c' and j == 2) :DP[j + 1][i + 1] += DP[i][j]
        if (S[j] == 'o' and j == 3) :DP[j + 1][i + 1] += DP[i][j]
        if (S[j] == 'd' and j == 4) :DP[j + 1][i + 1] += DP[i][j]
        if (S[j] == 'e' and j == 5) :DP[j + 1][i + 1] += DP[i][j]
        if (S[j] == 'r' and j == 6) :DP[j + 1][i + 1] += DP[i][j]



print(DP)

print(DP[len(rS)][len(S)] % (10**9+7))
