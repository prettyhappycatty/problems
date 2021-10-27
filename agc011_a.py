N, C, K = map(int, input().split())

T = []
for i in range(N):
    T.append(int(input()))

T.sort()
#print(T)

bus = []#時刻
cnt = [1]
i_bus = 0
bus.append(T[0]+K)
for i in range(1,N):
    #T[i]さんが乗るバスは
    if cnt[i_bus] < C and T[i] <= bus[i_bus]:
        cnt[i_bus] += 1
    else:
        i_bus += 1
        cnt.append(1)
        bus.append(T[i]+K)

#print(bus)
print(len(bus))
    

