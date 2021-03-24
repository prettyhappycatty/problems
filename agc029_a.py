S = input()

sum = 0
cnt = 0
for i in range(len(S)):
    #print(S[i], S[i]=='W')
    if S[i] == 'W':
        sum += cnt
    else:
        cnt += 1
print(sum)
