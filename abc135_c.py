N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

rest = 0
won = 0
for i in range(N):
    if A[i] > B[i] + rest:#まちにモンスターが残り、余力はない
        #print(A[i], '>', B[i] + rest)
        won += (B[i] + rest)
        rest = 0
    else:#次のまちのモンスターを倒せる余力が残る
        #print(A[i], '<', B[i] + rest)
        won += A[i]
        rest = B[i] + rest - A[i]
        if rest > B[i]:#モンスターが倒せるのは次の街までなので残せるのは今の攻撃力をMaxとする
            rest = B[i]
    #print(rest, won)


if A[N] > rest:
    #print(A[N], '>', rest)
    won += rest
else:
    #print(A[N], '<', rest)
    won += A[N]
#print(rest, won)

print(won)