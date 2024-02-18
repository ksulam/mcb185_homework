import random 

rolls = 100000
# rolling 6-sided die three times
total_1 = 0
for i in range(rolls):
	score = 0
	for i in range(3):
		d = random.randint(1, 6)
		score += d
	total_1 += score

print('3D6 Average:', total_1 / rolls)

# roll 3 6-sided die but reroll 1's	
total_2 = 0
for i in range(rolls):
	score = 0 #reset score for each roll
	for j in range(3):
		d = random.randint(1, 6)
		if d == 1:
			d = random.randint(1, 6)
		score += d	
	total_2 += score 
print('3D6r1 Average:', total_2 / rolls)

# roll pairs of six-sided 3 times, taking the maximum each time
total_3 = 0
for i in range(rolls):
	score = 0
	for j in range(3):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 > d2:
			score += d1
		else:
			score += d2
	total_3 += score

print('3d6x2 Average:', total_3 / rolls)


# roll 4 sided dice, dropping lowest die roll
total_4 = 0

for i in range(rolls):
	score = 0
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	d4 = random.randint(1, 6)

	if d1 <= d2 and d1 <= d3 and d1 <= d4: 
		score = score + d2 + d3 + d4
	elif d2 <= d1 and d2 <= d3 and d2 <= d4: 
		score = score + d1 + d3 + d4
	elif d3 <=d1 and d3 <= d2 and d3 <= d4: 
		score = score + d1 + d2 + d4
	else: 
		score = score + d1 + d2 + d3
	total_4 += score

print('4dr1 Averge:', total_4 / rolls)

