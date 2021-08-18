S = input()
a = []

right = {}
left = {}

cnt = 0
left[0] = 0
for i in range(len(S)):
    if S[i] == '<':
        cnt += 1
    else:
        cnt = 0
    left[i+1] = cnt

cnt = 0
right[len(S)] = 0
for i in range(len(S)-1, -1, -1):
    if S[i] == '>':
        cnt += 1
    else:
        cnt = 0
    right[i] = cnt

a_sum = 0
a_ary = []
#print(right, left)
for i in range(len(S)+1):
    a_sum += max(left[i], right[i])
    a_ary.append(max(left[i], right[i]))

#print(a_ary)

print(a_sum)    
        
        