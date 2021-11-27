N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sumA = [0]
sumB = [0]

for i in range(1,N+1):
    sumA.append(sumA[i-1]+A[i-1])

for i in range(1,M+1):
    sumB.append(sumB[i-1]+B[i-1])

#print(sumA)
#print(sumB)

ans=0
j=M
 
for i in range(N+1):
    #print("A-",i,j,N,M,len(sumA), len(sumB))
    if(sumA[i]>K):
        break
    while(sumA[i]+sumB[j]>K):
        #print(i,j,N,M)
        j-=1
    ans=max(ans,i+j)

print(ans)