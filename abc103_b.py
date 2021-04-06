S = input()
T = input()

s = 0
while s < len(S):
#    print(s)
    flg = 0
    for i in range(len(S)):
#        print(S[(s+i)%len(S)], T[i])
        if S[(s+i)%len(S)] != T[i]:
            flg = 1
            break
    
    if flg == 0:
        break
    
    s += 1

if flg == 0:
    print('Yes')
else:
    print('No')
        

