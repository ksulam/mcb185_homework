import random 

stable = 0
revive = 0
died = 0
live = 0

trials = 10000

for i in range(trials):
	dying = True
	failure = 0
	success = 0
	while dying:
		r1 = random.randint(1, 20)
		
		if r1 == 1:
			failure += 2		
		elif r1 == 20:
			dying = False
			revive += 1		
		else:
			if r1 < 10 and r1 > 1:
				failure += 1
			if r1 >= 10 and r1 < 20: 
				success += 1
		if dying:
			if failure >= 3:
				died += 1	
				dying = False
			if success == 3: 
				stable += 1
				dying = False

		
print('Probability of dying:', died / trials)
print('Probability of stabilizing:', stable / trials)
print('Probability of reviving:', revive / trials)


