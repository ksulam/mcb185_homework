import mcb185
import json
import gzip
import sys
import re

fulldict = []

with gzip.open(sys.argv[1], 'rt') as fp: #opening jaspar file
	singledict = {} #creating new dict for each ID
	
	for line in fp:  
		lines = line.rstrip()
		
		if line.startswith('XX'):
			continue
			
		if lines.startswith('ID'):
			singledict['id']= lines.split()[1] #ID name
			
			
		elif lines.startswith('PO'): #PWM data begins at this line
			singledict['pwm'] = [] 
			#print(singledict)
			
		#line starting with # = contains row of PWM values	
		elif lines.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
			splitpwm = line.split() #split pwm values in each row
			#print(splitpwm)
			
			#adding PWM values to singledict
			singledict['pwm'].append({'A': float(splitpwm[1]),
								'C': float(splitpwm[2]),
								'G': float(splitpwm[3]),
								'T': float(splitpwm[4])})
			
		#append data to fulldict + restarting dict for newID
		elif line.startswith('//'):
			fulldict.append(singledict)
			singledict = {}

#json format
jsonoutput = json.dumps(fulldict, indent=2)
#print(jsonoutput)
	

