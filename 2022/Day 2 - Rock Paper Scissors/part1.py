scoring = {"A":1, "B":2, "C":3, "win":6, "draw":3, "loss":0}

def getScore(a, b):
	if b=="X":
		b = "A"
	elif b=="Y":
		b = "B"
	else:
		b = "C"
	score = scoring[b]
	# Case for wins
	if ((b=="A" and a=="C") or (b=="B" and a=="A") or (b=="C" and a =="B")):
		#print(f"win {a} vs. {b}")
		score += scoring["win"]
	elif (a==b):
		#print(f"draw {a} vs. {b}")
		score += scoring["draw"]
	else:
		#print(f"loss {a} vs. {b}")
		score += scoring["loss"]
	return score

totalScore = 0
with open("input.txt", "r") as file:
	txt = file.readlines()
	for line in txt:
		line = line[:-1].split(" ")
		totalScore += getScore(line[0], line[1])
		
print(f"{totalScore=}")
