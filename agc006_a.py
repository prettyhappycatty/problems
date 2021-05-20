N = int(input())
S = input()
T = input()

check_words = []

for i in range(N):
    check_words.append(S[i:])

#print(check_words)

tmp_s = ''
for s in check_words:
    if T.find(s) == 0:
        tmp_s = s
        break

#print(tmp_s)

if len(tmp_s) == 0: #重なりがない
    print(len(S)+len(T))
else: #重なりがある
    print(len(S)+len(T) - len(tmp_s))