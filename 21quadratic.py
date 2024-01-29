import math

def quadratic(a, b, c):
	d = (b ** 2) - (4 * a * c) 
	
	if d < 0:  
		return None, None
	
	if d == 0: # when d=0, only get 1 solution
		x = (-b + math.sqrt(d)) / (2 * a)
		return x, x 

	else:
		x2 = (-b + math.sqrt(d)) / (2 * a)
		x1 = (-b - math.sqrt(d)) / (2 * a)
		return x1, x2

# testing function		
x1, x2 = quadratic(9, -12 ,4)
print(x1, x2)

x1, x2 = quadratic(1, 2, 1)
print(x1, x2)

x1, x2 = quadratic(-9, 2, 3)
print(x1, x2)

x1, x2 = quadratic(4, 2, 1)
print(x1, x2)