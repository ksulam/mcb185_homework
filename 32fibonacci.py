def fibonacci(n): 
	
	if n == 1 or n == 2:
		return 1 #first 2 numbers in fibonacci = 1
		
	return fibonacci(n - 1) + fibonacci(n - 2)

	
for i in range(1, 9): # print first 10 numbers in sequence 
	print(fibonacci(i))
		
	
	