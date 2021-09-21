N = int(input())
S = input()

S2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
dic = {}
for i in range(26):
    dic[S2[i]] = i

#print(dic)

ans = ""
for i in range(len(S)):
    #print((dic[S[i]]+N))
    ans += S2[(dic[S[i]]+N) % 26]

print(ans)