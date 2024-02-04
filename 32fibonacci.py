def fibonacci(n):
	n1 = -1
	n2 = 1
	
	for i in range(n):
		total = n1 + n2
		n1 = n2 #n1 takes on n2's prev. value
		n2 = total # n2 takes on value of n1+n2
		print(total)

fibonacci(10)