def temp(A, C, T, G):
	
	if A+C+T+G <= 13: 
		Tm = (A + T) * 2 + (G + C) * 4
	else:
		Tm = 64.9 + 41 * (G + C - 16.4) / (A + T + G + C)
	return Tm

print(temp(1, 2, 3, 4))
print(temp(20, 3, 3, 3))

		