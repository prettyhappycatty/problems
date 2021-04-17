S = input()
#print(len(S))
i = 0
cnt = 0
while i < len(S):
    if i == 0:
        bef = S[i]
        cnt = 1
    else:

        if bef == S[i] and i+1 < len(S):
            bef = S[i] + S[i+1]
            cnt += 1
            i +=1
        elif bef == S[i] and i+1 == len(S):
            bef == bef + S[i]
            cnt = cnt
        else:
            bef = S[i]
            cnt += 1

#    print(i, cnt, bef)
    i += 1
print(cnt)