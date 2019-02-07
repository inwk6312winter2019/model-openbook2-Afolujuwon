file1 = open('Street_Centrelines.csv','r')
file2 = open('Bus_Stops.csv','r')
stlist = []

def stClass():
	for line in file1:
		#line = line.split(',')
		if line[10] == 'ARTERIAL':
			if line[10].lower() not  in stlist:
				stlist.append(row['STR_NAME'].lower())
	print(stlist)

	count = 0
	for char in stlist:
		for line in file2:
			if char in line['LOCATION'].lower():
				if line['ACCESIBLE'] == 'Accessible':
					count = count + 1
			print(char + ':' + str(count))
stClass()
def stClass2():
	for line in file1:
		if line[10] == 'LOCAL STREET':
			if line[10].lower() not in stlist:
				stlist.append(row['STR_NAME'].lower())
	print(stlist)

	count = 0
	for char in stlist:
		for line in file2:
			if char in line['LOCATION'].lower():
				if line['ACCESIBLE'] == 'Accessible':
					count = count + 1
			print(char + ':' + str(count))
stClass2()
def stClass3():
	for line in file1:
		#line = line.split(',')
		if line[10] == 'MINOR COLLECTOR':
			if line[10].lower() not in stlist:
				stlist.append(row['STR_NAME'].lower())
	print(stlist)

	count = 0
	for char in stlist:
		for line in file2:
			if char in line['LOCATION'].lower():
				if line['ACCESIBLE'] == 'Accessible':
					count = count + 1
			print(char + ':' + str(count))
stClass3()
