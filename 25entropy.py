import math 
import sys

def shannon(a, t, c, g):
	total = a + t + c + g
	assert(total > 0) #total nt must be > 0
	
	aprob = a / total
	tprob = t / total
	cprob = c / total 
	gprob = g / total 
	
	if aprob <= 0: sys.exit('error: a must be greater than 0')
	aexp = aprob * math.log2(aprob)
		
	if tprob <= 0: sys.exit('error: t must be greater than 0')
	texp = tprob * math.log2(tprob)
	
	if cprob <= 0: sys.exit('error: c must be greater than 0')
	cexp = cprob * math.log2(cprob)
	
	if gprob <= 0: sys.exit('error: g must be greater than 0')
	gexp = gprob * math.log2(gprob)
	
 
	entropy = -(aexp + texp + cexp + gexp)
	return entropy

print(shannon(1, 2, 3 ,4))
print(shannon(0, 3, 6, 9))



