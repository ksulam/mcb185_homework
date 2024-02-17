import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d

def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val
	return mini
	

rgbinput = [R, G, B] 
colornames = []
dtclist = []

with open(colorfile) as fp:
	for line in fp:
		words = line.split()
		colornames.append(words[0])#create list for each color name
		
		colorvals = [] #create list of RGB values for a single color
		vals = words[2].split(",") #split RGB values from column 2 slice
		for val in vals: 
			colorvals.append(int(val)) 
			
		dtclist.append(dtc(colorvals, rgbinput)) #add dtc val to list for each color

  
mini_index = dtclist.index(minimum(dtclist)) #return index of mini value
print(colornames[mini_index]) #index of colors = index of mini  