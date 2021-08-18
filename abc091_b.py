N = int(input())
s = {}
for i in range(N):
    tmp = input()
    if tmp in s.keys():
        s[tmp] += 1
    else:
        s[tmp] = 1

M = int(input())
t = {}
for i in range(M):
    tmp = input()
    if tmp in t.keys():
        t[tmp] += 1
    else:
        t[tmp] = 1


#print(s,t)
s = sorted(s.items(), key=lambda x:x[1], reverse=True)
#t = sorted(t.items(), key=lambda x:x[1], reverse=True)

word = ''
m = 0
for i in range(len(s)):
    if s[i][0] in t.keys():
        tmp_m = s[i][1] - t[s[i][0]]
    else:
        tmp_m = s[i][1]
        
    if tmp_m > m:
        m = tmp_m
    #print(s[i][0], s[i][1])
#print(s,t)
print(m)
