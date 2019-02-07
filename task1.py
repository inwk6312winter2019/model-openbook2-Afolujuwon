file = open('Street_Centrelines.csv')

def tupls():
	for line in file:
		line = line.split(',')
		output1 = (line[2],line[3],line[6],line[7])
		print("tuple of STR_NAME,FULL_NAME,FROM_STR,TO_STR is:",output1)

#tupls()

def dictionary():
	for line in file:
		line = line.split(',')
		output2 = zip(line[12],line[0])
		print(dict(output2))

#dictionary()

def uOwners():
	for line in file:
		line = line.split(',')
		print(line[11])
#uOwners()

def stClass():
	for line in file:
		line = line.split(',')
		if line[10]=='ARTERIAL':
			char = line.join()
			print(char)
stClass()
