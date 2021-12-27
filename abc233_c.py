import copy

N, X = map(int, input().split())

balls = {i:[] for i in range(N)}
balls_cnt = []

comb_cnt = 1

for i in range(N):
    tmp = list(map(int, input().split()))
    balls[i]= tmp[1:]
    balls_cnt.append(tmp[0])
    comb_cnt *= tmp[0]

#print(balls)

#行列の計算を作る
def dot(ary1, ary2):
    retary = []
    for i in range(len(ary1)):
        for j in range(len(ary2)):
            retary.append(ary1[i]*ary2[j])
    return retary

newary = [1]
for i in range(N):
    #print(newary, balls_cnt[i])
    newary = dot(newary, balls[i])


cnt = 0
for i in range(len(newary)):
    if newary[i] == X:
        cnt += 1

print(cnt)