
N, A, B, C, D = map(int, input().split())
S = input()
A,B,C,D = A-1, B-1,C-1,D-1
l = [A,B,C,D]

def isRock2(SS):#2連続以上の岩があるか
    S = SS[A:C+1]
    if "##" in S:
        #print("AC")
        return False
    S = SS[B:D+1]
    if "##" in S:
        #print("BD")
        return False
    return True

def isMasu2(SS):#入れ替わるのに必要な3マス空きがあるか
    SS = SS[min(l):max(l)+1]
    SS = SS[B:D]
    if "..." in SS:
        return True
    return False

#print(S)
#print(isMasu2(S), isRock2(S))

if C > D: #スタートとゴールですぬけくんとふぬけくんが入れ替わる
    if isMasu2(S) == True and isRock2(S) == True:
        print("Yes")
        exit()
    else:
        print("No")
else:
    if isRock2(S) == True:
        print("Yes")
        exit()
    else:
        print("No")
