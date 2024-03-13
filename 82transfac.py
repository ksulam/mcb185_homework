import mcb185
import json
import gzip
import sys
import re

catalog = [] #creating empty catalog of records for pwm

with gzip.open(sys.argv[1], 'rt') as fp: #opening jaspar file
	singlerecord = {} #creating new record of pwm for a single ID
	
	for line in fp:  
		lines = line.rstrip() #remove characters from the end
		#print(lines)
		
		if lines.startswith('ID'):
			singlerecord['id']= lines.split()[1] #ID name
			
			
		elif lines.startswith('PO'): #PWM data begins at this line
			singlerecord['pwm'] = [] #empty pwm
			#print(singlerecord)
	
			
		#line starting with # = contains row of PWM values	
		elif lines.startswith(('0')):
			splitpwm = line.split() #split pwm values in each row
			#print(splitpwm)
			
			#adding PWM values to singlerecord
			singlerecord['pwm'].append({'A': float(splitpwm[1]),
								'C': float(splitpwm[2]),
								'G': float(splitpwm[3]),
								'T': float(splitpwm[4])})
			
		#append data to catalog + restarting record for newID
		elif line.startswith('//'):
			catalog.append(singlerecord)
			singlerecord = {}

#json format
jsoncatalog = json.dumps(catalog, indent=2)
print(jsoncatalog)
	

