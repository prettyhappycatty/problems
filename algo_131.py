S = 0b01001

cnt = 0
while S > 0:
	mod = S & 0b1 #下1桁マスク
	if mod == 1:
		cnt += 1
	S = S >> 1 #1ビットシフト

print(cnt)