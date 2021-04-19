S = input()

now = ''
bai = ''

def isGood(S):
    S1 = S[0:len(S)//2]
    S2 = S[len(S)//2:]
    if S1 == S2:
        return True
    else:
        return False

new_S = S
for i in range(len(S)):
    new_S = new_S[:-1]
    #print(-i, new_S)
    if isGood(new_S):
        #print(new_S)
        break

print(len(S)-i-1)