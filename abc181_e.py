N, M = map(int, input().split())
H = list(map(int, input().split()))
W = list(map(int, input().split()))

H.sort()
#print("H",H)

W.sort()
#print("W",W)

sub_plus=[0]
sub_minus=[0]

sub_p = 0
sub_m = 0
for i in range(0, N//2):
    sub_p += abs(H[2*i+1]-H[2*i])
    sub_plus.append(sub_p) #奇数-偶数

for i in range(0, N//2):
    sub_m += abs(H[2*i+2]-H[2*i+1])
    sub_minus.append(sub_m) #偶数-奇数

#print(sub_minus, sub_plus)

#尺取法で対象となる人と一番差が小さくなるものをメモ
w_sub = []
i,j = 0,0
bef = 10**9
while i < N and j < M:
    #print(i,j)
    while bef >= abs(H[i] - W[j]):
        bef = abs(H[i]-W[j])
        j += 1
        if j == M:
            break
    w_sub.append(bef)
    bef = 10**9
    i += 1
    j -= 1

if i < N:
    j = j-1

while i < N:
    #print(i,j)
    w_sub.append(abs(H[i]-W[j]))
    i += 1


#print(w_sub)

def get_i_sum(i):
#    print(i,sub_minus[-1],"-",sub_minus[i],"+", sub_plus[i],"+", w_sub[2*i],sub_minus[-1]-sub_minus[i] + sub_plus[i] + w_sub[2*i])
    return sub_minus[-1]-sub_minus[i] + sub_plus[i] + w_sub[2*i]

ans = 10**9

for i in range(N//2+1):
    j = i*2
    #print("-",j,"-")
    ans = min(get_i_sum(i), ans)


print(ans)