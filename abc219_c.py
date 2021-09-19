X = input()
N = int(input())
X1 = "abcdefghijklmnopqrstuvwxyz"

S = []
for i in range(N):
    tmpS = input()
    S.append(tmpS)


dic = {}
dic2 = {}
for i in range(len(X)):
    dic[X[i]] = i
    dic2[i] = X1[i]

#print(dic)
#print(dic2)

newS = {}
#print(S)
for i in range(len(S)):
    st = ""
#    print(S[i])
    for j in range(len(S[i])):
#        print(dic[S[i][j]])
        #priznt(dic2[dic[S[i][j]]])
        st += dic2[dic[S[i][j]]]
    newS[S[i]] = st

sorted_new = list(sorted(newS.items(), key=lambda x:x[1]))

for i in range(len(sorted_new)):
    print(sorted_new[i][0])
#print(sorted_new)
    
