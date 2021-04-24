N = int(input())
S = list(input())
Q = int(input())

S1 = S[:len(S)//2]
S2 = S[len(S)//2:]

def swapType1(i,j,s1,s2):#i番目とj番目を入れ替える時
    #print(i,j-len(s1),s1,s2)
    if i < len(s1) and j < len(s1):
        s1[i], s1[j] = s1[j],s1[i]
    elif i < len(s1) and len(s1) <= j:
        s1[i], s2[j-len(s1)] = s2[j-len(s1)],s1[i]
    else:# len(s)//2 =< i and len(s)//2 =< j:
        s2[i-len(s1)], s2[j-len(s1)] = s2[j-len(s1)],s2[i-len(s1)]
    return s1,s2

def swapType2(s1, s2):
    return s2,s1


for i in range(Q):
    tmpT, tmpA, tmpB = list(map(int, input().split()))
    #print(tmpA-1, tmpB-1)
    if tmpT == 1:
        S1,S2 = swapType1(tmpA-1,tmpB-1,S1,S2)
    elif tmpT == 2:
        S1,S2 = swapType2(S1,S2)

newS1 = ''.join(S1)
newS2 = ''.join(S2)

print(newS1+newS2)