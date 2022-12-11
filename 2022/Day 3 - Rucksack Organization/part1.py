filename = "input"

def getPriorityOfChar(c):
	if (c == c.lower()):
		return(ord(c) - 96)
	return(ord(c) - 38)
		
def findError(rucksack):
	compSize = len(rucksack) // 2
	comp1, comp2 = rucksack[:compSize], rucksack[compSize:]
	assert(len(comp1) == len(comp2))
	
	err = ''
	for c in comp1:
		if c in comp2:
			err = c
			break
	
	
	return getPriorityOfChar(err)


txt = ""
with open(filename + ".txt", "r") as file:
	txt = file.readlines()
	for index,value in enumerate(txt):
		txt[index] = txt[index][:-1]

sum = 0
for sack in txt:
	sum += findError(sack)


print(f"{sum=}")