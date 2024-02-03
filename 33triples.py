import math
def is_perfect_square(n):
	root = math.sqrt(n)
	if root % 1 == 0: return True
	return False

def isinteger(n):
	if n == n // 1: return True
	return False
count = 0
    	
for a in range(1, 101): 
	for b in range(a+1, 101):
		csquared = a ** 2 + b ** 2
		if is_perfect_square(csquared) == True:
			print(a, b, int(math.sqrt(csquared)))
			count = count + 1
				
print("total perfect triples: ", count)