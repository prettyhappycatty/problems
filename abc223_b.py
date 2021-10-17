S = input()

ary_S = []
for i in range(len(S)):
    tmp_S = ""
    for j in range(len(S)):
        tmp_S += S[(i+j)%len(S)]
    ary_S.append(tmp_S)

ary_S.sort()

print(ary_S[0])
print(ary_S[len(S)-1])