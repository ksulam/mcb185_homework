import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

bdaymatch = 0

for i in range(trials):
	calendar = [] # making calendar
	for i in range(days):
		calendar.append(0) 
	
	for i in range(people):
		date = random.randint(0, days - 1) # fill calendar with dates
		calendar[date] += 1 

	shared = False
	for count in calendar:
		if count >= 2:
			shared = True
			break
				
	if shared: 
		bdaymatch += 1 #when find a bday match break loop and add to count

print(bdaymatch / trials)