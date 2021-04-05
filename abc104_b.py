S = input()

flg = 0
cntA = 0
cntC = 0
cntOther = 0
if 4 <= len(S) <= 10:

    for i in range(len(S)): 
        if i == 0 and S[i] == 'A':
            cntA = 1

        if 2 <= i <= len(S)-2 and S[i] == 'C':
            cntC += 1
        #print(S[i], S[i].islower())
        if S[i].islower():
            cntOther += 1

#print(cntA, cntC, cntOther)
if cntA == 1 and cntC == 1 and cntOther == len(S)-2:
    print('AC')
else:
    print('WA')