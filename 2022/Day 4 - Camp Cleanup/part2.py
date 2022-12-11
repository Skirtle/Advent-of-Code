filename = "input"


def findOverlaps(pair):
	elves = pair.split(",")
	elf1 = list(map(int, elves[0].split("-")))
	elf2 = list(map(int, elves[1].split("-")))
	
	elf1Overlaps = elf2[1] in range(elf1[0], elf1[1] + 1) or elf1[1] in range(elf2[0], elf2[1] + 1)
	elf2Overlaps = elf2[0] in range(elf1[0], elf1[1] + 1) or elf1[0] in range(elf2[0], elf2[1] + 1)
	
	# Elf starting section in range of other elf
	if (elf1Overlaps or elf2Overlaps):
		return True
	return False

txt = ""
with open(filename + ".txt", "r") as file:
	txt = file.readlines()
	for index,value in enumerate(txt):
		txt[index] = txt[index][:-1]

sum = 0
for pair in txt:
	sum += findOverlaps(pair)
print(f"{sum=}")
if (filename == "test"):
	assert(sum == 4)