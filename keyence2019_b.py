S = input()

keyence = 'keyence'

flg = False

for start in range(len(S)-1):
    for end in range(start, len(S)):
        st = S[0:start] + S[end:len(S)]
        if st == keyence:
            flg = True

if flg == True:
    print("YES")
else:
    print("NO")
