N = int(input())
S = input()

rS = "atcoder"
DP = [[0 for i in range(N+1)] for j in range(len(rS)+1)]

#print(DP)
print("a  t  t  c  o  r  d  e  e  r")
for j in range(len(rS)):
    for i in range(len(S)):
        #print(S[i], rS[j],DP[j+1][i+1],DP[j][i])
        if S[i] == rS[j]:
            if j == 0:
                DP[j][i] += 1
            print(j,i,j+1, i+1)
            DP[j+1][i+1] += DP[j][i]
            #DP[j][i+1] = DP[j][i+1] + DP[j][i]
            #DP[i+1][j+1] = DP[i+1][j+1]
        DP[j][i+1] = DP[j][i]
    print(DP[j])

#print(DP)
