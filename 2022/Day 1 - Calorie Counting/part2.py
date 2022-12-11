elves = []

with open("input.txt", "r") as file:
	txt = file.readlines()
	elfNum = 0
	elfCals = 0
	for line in txt:
		if line=="\n":
			elfNum += 1
			elves.append((elfNum, elfCals))
			elfCals = 0
		else:
			elfCals += int(line[:len(line)-1])

elves.sort(key = lambda  x : x[1], reverse = True)
topElves = elves[:3]

sum = 0
print("The top three elves are [", end = "")
for elf in topElves:
	print(" " + str(elf[0]), end = "")
	sum += elf[1]
print(" ], carrying a total of " + str(sum))
