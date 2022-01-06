N, M, K = map(int, input().split())

#2, 2, 2
#0, 1, or 1, 0 or 1, 1

#3, 2, 3
#(1, 0)
# ###
# ...
#(0, 1)
# #..
# #..
#縦何個、横何個押すかで場所や順番は関係ない

if K == 0:
    print("Yes")
    exit()

for i in range(N):
    for j in range(M):
        b = i*j + (N-i)*(M-j)
        if b == K:
            print("Yes")
            exit()

print("No")


