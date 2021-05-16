
N = int(input())
S = input()
T = input()

cnt_s_1 = 0
cnt_t_1 = 0
diff = 0

s_ar = []
t_ar = []

for i in range(N):
    if S[i] != T[i]:
        diff+= 1
    if S[i] == '0':
        s_ar.append(i)
        cnt_s_1 += 1
    if T[i] == '0':
        t_ar.append(i)
        cnt_t_1 += 1

and_set = set(s_ar) ^ set(t_ar)
print(s_ar)
print(t_ar)
print(and_set)

if cnt_s_1 == cnt_t_1:
    print(len(and_set))
else:
    print(-1)
#print(cnt_s_1, cnt_t_1, diff, s_group_1,  t_group_1, diff_group_diff)
'''
N = int(input())
S = input()
T = input()
A = [0 for i in range(500000)]
B = [0 for i in range(500000)]
cntA = 0
cntB = 0
Answer = 0
 
for i in range(N):
    if S[i] == '0':
        A[cntA] = i
        cntA += 1
    if T[i] == '0':
        B[cntB] = i
        cntB += 1
 
if cntA != cntB:
    print("-1")
else:
    for i in range(cntA):
        if A[i] != B[i]:
            Answer += 1
    print(Answer)
'''