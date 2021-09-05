#ひっくり返される数は、neighborの個数+そのものの個数。
#幅と高さが両方2以上の場合
#角=4, 辺=6, 真ん中=9
#幅も高さも1の場合　1回しか起こらないので、1
#幅と高さがどちらかが1の場合
#角=2, 辺=3, 真ん中なし


# N < M としてしまう。
M, N = map(int, input().split())

#swapしてN<Mとしておく
if M < N:
    tmp = N
    N = M
    M = tmp

if N == 1 and M == 1:
    print(1)
elif N == 1:
    print(M-2)
else:
    print((N-2)*(M-2))

