S = input()

odd = 0
even = 0
for i in range(len(S)-1, -1, -1):
    j = len(S)-i
    if j % 2 == 0:
        even += int(S[i])
    else:
        odd += int(S[i])

print(even, odd)