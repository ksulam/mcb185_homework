def factorial(n):
	if n == 0: 
		return 1
	fac = 1
	for i in range (1, n + 1):
		fac = fac * i 
	return fac 

def nchoosek(n, k):
	return factorial(n) / (factorial(k) * factorial(n - k))
		
print(nchoosek(5, 3))
print(nchoosek(10, 2))