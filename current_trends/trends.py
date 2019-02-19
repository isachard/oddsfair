
def fileHandling(someFile):
    with open(someFile) as f:
        lines = f.read().splitlines()
        return lines

def addition(bet, update):
	dictionary[bet]= dictionary[bet] + int(update )

def subtraction(bet, update):
	dictionary[bet]= dictionary[bet] - int(update)

def cuenta():
	count = 0

	for k,v in dictionary.items():
		print(k,v, end=" | " )
		
		if k[1] == "8":
			print()
	
		count = count + v
		
	print("\n \nTotal in the league: $" + str(count))


def mathAlgo(fileProvided):
	for bet in fileProvided:
		bet = bet.split()
		if bet[1] == "l":
			subtraction(bet[0],bet[2])
		else:
			addition(bet[0], bet[2])

def spreadLosers():
	count = 0 
	for k,v in dictionary.items():
		if k[0] == "l"[0]:
			count = count + v

	return count


def spreadWinners():
	count = 0 
	for k,v in dictionary.items():
		if k[0] == "w"[0]:
			count = count + v	
	return count

def totalUnders():
	count = 0 
	for k,v in dictionary.items():
		if k[0] == "u"[0]:
			count = count + v
	return count

def totalOvers():
	count = 0 
	for k,v in dictionary.items():
		if k[0] == "o"[0]:
			count = count + v
	return count

def printdictionary():
	print("\n--------|League stats NBA/NHL 2018-2019 SEASON|--------\n")
	print("\nNBA: \n")
	fileListed = fileHandling(nba)
	mathAlgo(fileListed)
	cuenta()
	spreadL = spreadLosers()
	print("Losers Total: $" + str(spreadL)) 
	spreadW = spreadWinners()
	print("Winners Total: $" + str(spreadW))
	print("\nSpread Overall" + str(spreadW + spreadL), end="\n\n")
	
	totalU = totalUnders()
	print("Unders Total: $" + str(totalU)) 

	totalO = totalOvers()
	print("Overs Total: $" + str(totalO)) 
	print("\nTotals Overall $" + str(totalU + totalO), end="\n\n")


	setDictToZero()
	
	print("\nNHL: \n") 
	fileListed = fileHandling(nhl)
	mathAlgo(fileListed)
	cuenta()
	totalU = totalUnders()
	print("Unders Total: $" + str(totalU)) 

	totalO = totalOvers()
	print("Overs Total: $" + str(totalO)) 
	print()

def setDictToZero():
	global dictionary
	dictionary = dictionary.fromkeys(dictionary,0)





spreadValue = 0 
totalValue = 0 
nba = "nbadata.txt"
nhl = "nhldata.txt"
defaultValue = 0 
dictionary = dict.fromkeys(['w4*','u3','l7*','l3','w3','o3','l4','l5','l6','l7','l8','w4','w5','w6','w7','w8','u4','u5','u6','u7','u8','o4','o5','o6','o7','o8','u3*','u4*','l4*','l5/','w5/','l6*','o4*','o6*'], defaultValue)


printdictionary()








