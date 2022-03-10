A,B,C,D = map(int, input().split())

primes = set((2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199))


takahashi = [i for i in range(A,B+1)]
aoki = [i for i in range(C,D+1)]

#print(primes)
#print(takahashi, aoki)
#最適な戦略とは
#高橋くんは、青木くんが何を選んでも素数にならない数を選びたい。-> なければ負け。
#青木くんは高橋くんが選んだ数で素数が作れれば勝ち。


def check_plusaoki(x):
    for a in aoki:
        if a+x in primes:
            return False
    return True

for t in takahashi:
    if check_plusaoki(t):
         print("Takahashi")
         exit()

print("Aoki")
