S = input()

i = 0
bef = ''
gl_cnt = 0
cnt = 0

while i < len(S):
    if i > 0 and bef != S[i]:
        gl_cnt += (1 + cnt)*(cnt)/2
        print(cnt, (1+cnt)*(cnt)/2, gl_cnt)
        cnt = 0
    bef = S[i]
    i += 1
    cnt += 1

print(gl_cnt)