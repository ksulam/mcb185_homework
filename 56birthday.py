
#gather all bday, do half matrix-major diagonal
# or sort and look for duplicate
import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

matching = 0 

for trial in range(trials): 
	
	bdays = []
	for i in range(people):
		date = random.randint(1, days)
		bdays.append(date)
	
	shared = False 
	bdays.sort() # sort bdays numerically 
	for i in range(1, len(bdays)):
		if bdays[i - 1] == bdays[i]:
			shared = True
			break   # stop when first bday match is found 
	
	if shared == True: matching += 1 # add to count when shared is true 
	
		
print(matching / trials)
