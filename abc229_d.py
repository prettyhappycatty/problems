S = input()
K = int(input())

#累積和
sharp = [0]
colon = [0]
sharp_sum = 0
colon_sum = 0
for i in range(len(S)):
    if S[i] == "X":
        sharp_sum += 1
    else:
        colon_sum += 1
    sharp.append(sharp_sum)
    colon.append(colon_sum)

#print(sharp)
#print(colon)

i, j = 0, 1
ans = 0
while j < len(S)+1:
    if colon[j]-colon[i] <= K:
        ans = max(ans,sharp[j]-sharp[i]+colon[j]-colon[i])
        j += 1
    else:
        i += 1

print(ans)
    

    