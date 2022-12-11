filename = "input"

def getPriorityOfChar(c):
	if (c == c.lower()):
		return(ord(c) - 96)
	return(ord(c) - 38)


def findBadges(rucksackGroup):
	badge = ""
	for c in rucksackGroup[0]:
		if c in rucksackGroup[1] and c in rucksackGroup[2]:
			badge = c
			return getPriorityOfChar(badge)


txt = ""
with open(filename + ".txt", "r") as file:
	txt = file.readlines()
	for index,value in enumerate(txt):
		txt[index] = txt[index][:-1]

sum = 0
for i in range(3, len(txt) + 1, 3):
	group = txt[i-3: i]
	sum += findBadges(group)


print(f"{sum=}")