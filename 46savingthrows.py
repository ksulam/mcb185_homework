import random 

def normal(): 
	r1 = random.randint(1, 20)
	return r1 

# if have advantage, roll 2 dice, receive higher number of points 
def advantage():
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	if r1 >= r2:
		return r1
	else: 
		return r2 

# if have disadvantage, roll 2 dice, receive lower number of points 		
def disadvantage():
	r1 = random.randint(1, 20)
	r2 = random.randint(1, 20)
	if r1 <=r2:
		return r1
	else:
		return r2

trials = 10000		

print("normal")
for dc in range(5, 16, 5):
	print(dc, end='\t')
	success = 0
	for i in range(trials):
		roll = normal()
		if roll > dc:
			success += 1
	print(success / trials)

print("advantage")
for dc in range(5, 16, 5):
	print(dc, end='\t')
	success = 0
	for i in range(trials):
		roll = advantage()
		if roll > dc:
			success += 1
	print(success / trials)

print("disadvantage")	
for dc in range(5, 16, 5):
	print(dc, end='\t')
	success = 0
	for i in range(trials):
		roll = disadvantage()
		if roll > dc:
			success += 1
	print(success / trials)


		
		
		
		
		
		
		