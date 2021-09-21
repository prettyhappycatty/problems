S = input()

cnt = 0
for i in range(len(S)//2):#奇数の場合も切り捨てる
    if S[i] != S[len(S)-i-1]:
        cnt += 1

print(cnt)