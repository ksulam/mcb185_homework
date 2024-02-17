
#gather all bday, do half matrix-major diagonal
# or sort and look for duplicate
import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

bdaymatch = 0 

for i in range(trials):
	bdays = []
	
	for j in range(people):
		date = random.randint(1, days)
		bdays.append(date) # generate class bdays 
		
	shared = False
	for i in range(len(bdays)): 
		for j in range(i + 1, len(bdays)):
			if bdays[i] == bdays[j]:
				shared = True
				
	if shared: 
		bdaymatch += 1 #when find a bday match break loop and add to count

print(bdaymatch / trials)