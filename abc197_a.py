S = input()

S_r = ''

for i in range(1, len(S)):
    S_r += S[i]
S_r += S[0]

print(S_r)
