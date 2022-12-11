filename = "input"

scoring = {"X":6, "Y":3, "Z":0, "rock":1, "paper":2, "scissors":3}

def getScore(a, b):
	if (a == "A" and b == "Z"): # Winning against rock
		return(6 + 2)
	elif (a == "B" and b == "Z"): # Winning against paper
		return(6 + 3)
	elif (a == "C" and b == "Z"): # Winning against scissors
		return(6 + 1)
	elif (a == "A" and b == "Y"): # Draw against rock
		return(3 + 1)
	elif (a == "B" and b == "Y"): # Draw against paper
		return(3 + 2)
	elif (a == "C" and b == "Y"): # Draw against scissors
		return(3 + 3)
	elif (a == "A" and b == "X"): # Loss against rock
		return(0 + 3)
	elif (a == "B" and b == "X"): # Loss against paper
		return(0 + 1)
	elif (a == "C" and b == "X"): # Loss against scissors
		return(0 + 2)

totalScore = 0
with open(filename + ".txt", "r") as file:
	txt = file.readlines()
	for line in txt:
		line = line[:-1].split(" ")
		# print(getScore(line[0], line[1]))
		totalScore += getScore(line[0], line[1])


print(f"{totalScore=}")
if (filename == "test"):
	assert(totalScore == 12)
