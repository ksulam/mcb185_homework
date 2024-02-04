def fibonacci(n):
	n1 = -1
	n2 = 1
	
	for i in range(n):
		n3 = n1 + n2
		n1 = n2 #n1 takes on n2's prev. value
		n2 = n3 # n2 takes on value of n1+n2
		print(n3)

fibonacci(10)