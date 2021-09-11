N = int(input())

T, S = [], []
for i in range(N):
    tmpS = input()
    S.append(tmpS)

for i in range(N):
    tmpT = input()
    T.append(tmpT)

#print(S, T)

# 90度回転
S90, S180, S270 = [], [], []
for i in range(N):
    tmp_S90, tmp_S180, tmp_S270 = [], [], []
    for j in range(N):
        tmp_S90.append(S[-j-1][i])
        tmp_S180.append(S[-i-1][-j-1])
        tmp_S270.append(S[j][-i-1])
    S90.append(tmp_S90)
    S180.append(tmp_S180)
    S270.append(tmp_S270)

#print(S270)


#平行移動
def check(S1, T1, ki, kj):#S1をki, kj移動したものに一致するかを返す
    #またがるものをはねるため
    bound_si_min = N
    bound_si_max = -1
    bound_sj_min = N
    bound_sj_max = -1
    bound_ti_min = N
    bound_ti_max = -1
    bound_tj_min = N
    bound_tj_max = -1
    for i in range(N):
        for j in range(N):
            if S1[(i + ki) % N][(j + kj)% N] == "#":
                bound_si_min = min(bound_si_min, (i + ki) % N)
                bound_si_max = max(bound_si_max, (i + ki) % N)
                bound_sj_min = min(bound_sj_min, (j + kj) % N)
                bound_sj_max = max(bound_sj_max, (j + kj) % N)
            if T1[i][j] == "#":
                bound_ti_min = min(bound_ti_min, i)
                bound_ti_max = max(bound_ti_max, i)
                bound_tj_min = min(bound_tj_min, j)
                bound_tj_max = max(bound_tj_max, j)
            if S1[(i + ki) % N][(j + kj)% N] != T1[i][j]:#平行移動した結果どれか一つでも違ったらFalse
                return False
    #print(ki,kj)

    #print(bound_si_max,bound_si_min, bound_ti_max,bound_ti_min)
    #print(bound_sj_max,bound_sj_min, bound_tj_max,bound_tj_min)

    if bound_si_max - bound_si_min == bound_ti_max - bound_ti_min and bound_sj_max - bound_sj_min == bound_tj_max - bound_tj_min:
       return True#全部一致ならTrue
    else:
        return False

for i in range(N):
    for j in range(N):
        if check(S, T, i, j) == True or check(S90, T, i, j) == True or check(S180, T, i, j) == True or check(S270, T, i, j) == True:
            print("Yes")
            exit()

print("No")