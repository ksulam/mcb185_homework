import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])
rgbinput = [R, G, B]

colornames = []
dtclist = []

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


with open(colorfile) as fp:
	for line in fp:
		words = line.split()
		colornames.append(words[0])#first column = name of colors
		
		colorvals = [] #create list of RGB values for a single color
		vals = words[2].split(",")
		for val in vals: 
			colorvals.append(int(val)) 
			
		dtclist.append(dtc(colorvals, rgbinput)) #add dtc val to list for each line

  
idx = dtclist.index(minimum(dtclist)) #return index of the fist mini value
print(colornames[idx]) #index of colors = index of dtc  