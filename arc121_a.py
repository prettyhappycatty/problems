N = int(input())

P =[] 
for i in range(N):
    P.append(tuple(map(int, input().split()))) 

#print(P)

def chev(P1, P2):
    return max(abs(P1[0]-P2[0]), abs(P1[1]-P2[1]))

max_chev_1 = 0
max_chev_2 = 0

for i in range(N-1):
    for j in range(i+1, N):
        chev_dist = chev(P[i], P[j])
        if max_chev_1 < chev_dist:
            max_chev_2 = max_chev_1
            max_chev_1 = chev_dist
        elif max_chev_2 < chev_dist:
            max_chev_2 = chev_dist
        #print(chev_dist, max_chev_1, max_chev_2)

print(max_chev_2)
