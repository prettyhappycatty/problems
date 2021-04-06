S = input()

s = 0
e = len(S)-1
s_c = -1
e_c = len(S)
while True:
    if S[s] == 'A':
        s_c = s
    else:
        s += 1
    if S[e] == 'Z':
        e_c = e
    else:
        e -= 1
    if s_c > -1 and e_c < len(S):
        break

print(e_c - s_c + 1)

