import os

directory = "CSV_Stats/"
for filename in os.listdir(directory):
	nameString = filename
	count = 0
	for char in nameString:
		if(char.isdigit()):
			nameString = nameString[:count] + nameString[count+1:]
			continue
		nameString = nameString[:count] + char.lower() + nameString[count+1:]
		count += 1
	os.rename(directory+filename, directory+nameString)
	print(nameString)