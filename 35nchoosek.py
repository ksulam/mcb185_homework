def factorial(n):
	if n == 0 or n == 1:
		return 1
		
	else: 
		return n * factorial(n - 1)
		
def solve(n, k):
	if k < 0 or k > n:
		return 0
	else:
		return factorial(n) // (factorial(k) * factorial(n - k))

print(solve(10, 2))
print(solve(31, 4))
print(solve(12, 3))