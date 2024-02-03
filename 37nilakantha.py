def nilakantha(number):
	pi = 3.0
	sign = 1
	
	for i in range(1, number):
		denom = 2 * i * (2 * i + 1) * (2 * i + 2)
		order = 4 / denom
		pi = pi + sign * order
		sign = sign + (-1)
		
	return pi 
		
print(nilakantha(2))
print(nilakantha(6))
	