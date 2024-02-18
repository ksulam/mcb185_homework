import random
import math 

insidecount = 0
outsidecount = 0
total = 0 

while True:
	total += 1
	x = random.random()
	y = random.random()
	length = math.sqrt(x**2 + y**2) 

	if length < 1:
		insidecount += 1
	
	ratio = 4 * insidecount / total
	print(ratio)

  

# gen random int