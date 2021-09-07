b = 0b011101 & 0b11001

cnt = 0
while b > 0:
	mod = b & 0b1 #下1桁マスク
	if mod == 1:
		cnt += 1
	b = b >> 1 #1ビットシフト

print(cnt)