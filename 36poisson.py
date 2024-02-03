import math

def poisson(n, k):
	probability = (n ** k * math.exp(-n)) / math.factorial(k)
	return probability
	
print(poisson(1, 2))
print(poisson(5, 8))