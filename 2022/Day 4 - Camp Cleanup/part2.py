filename = "input"


def findContainments(pair):
	elves = pair.split(",")
	elf1 = list(map(int, elves[0].split("-")))
	elf2 = list(map(int, elves[1].split("-")))
	
	# elf1 contains elf2 OR elf2 contains elf1
	if ((elf2[0] >= elf1[0] and elf2[1] <= elf1[1]) or elf1[0] >= elf2[0] and elf1[1] <= elf2[1]):
		return True
	return False

txt = ""
with open(filename + ".txt", "r") as file:
	txt = file.readlines()
	for index,value in enumerate(txt):
		txt[index] = txt[index][:-1]

sum = 0
for pair in txt:
	sum += findContainments(pair)
print(f"{sum=}")
if (filename == "test"):
	assert(sum == 2)