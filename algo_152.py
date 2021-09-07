b = 0b10001

cnt = 0
s = ""
while b > 0:
	mod = b & 0b1 #下1桁マスク
	mod_not = ~mod & 0b1
	s = s + str(mod_not)
	b = b >> 1 #1ビットシフト

print(s)