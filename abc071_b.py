S = input()

S_ = 'abcdefghijklmnopqrstuvwxyz'
in_S = {}

for s in S_:
    in_S[s] = 1

for s in S:
    in_S[s] = 0

cnt = 0
first = ''
for ss in in_S:
    if in_S[ss] == 1:
        first = ss
        cnt += 1
        break

if cnt == 0:
    print('None')
else:
    print(first)

