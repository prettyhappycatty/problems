N, M = map(int, input().split())

ship = set()

for i in range(M):
    a, b = map(int, input().split())
    ship.add(tuple((a-1,b-1)))

#print(ship)

#0-index
for i in range(1, N):
#    print(ship.count(set((0,i))) , ship.count(set((i,N-1))))
    if tuple(([0,i])) in ship and tuple(([i,N-1])) in ship:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")
    
