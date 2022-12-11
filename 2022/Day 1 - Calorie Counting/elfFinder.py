elves = []

with open("input.txt", "r") as file:
	txt = file.readlines()
	elfNum = 0
	elfCals = 0
	for line in txt:
		if line=="\n":
			elfNum += 1
			elves.append(elfCals)
			elfCals = 0
		else:
			elfCals += int(line[:len(line)-1])

highestCals = 0
highElf = 0
for elf,cals in enumerate(elves):
	if (cals > highestCals):
		highElf = elf + 1
		highestCals = cals

print(f"Elf {highElf} has the highest with {highestCals}")