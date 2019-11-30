string = ""
file = input("nom du fichier?")
f = open (file+".txt", "r")
lines = f.readlines()
ici = False
for x in lines:
	if "invariant"in x:
		ici = True
	else:
		if "T-SEMI-FLOWS" in x:
			ici = False
	if ici == True:
		string +=x
tabplace = []
for x in range(0,len(string)):
	startsemi = 0
	poid = 0
	nbinvar = 0;
	char = string[x]
	semistart = 0
	if char == "(":
		poid = int(string[x+1])
		nbinvar += 1
		bufsemi = ""
		tabcouple = []
		nbplace = 0;
		for a in range(0,x):
			bufsemi = bufsemi + string[a+semistart]
			if string[a+semistart] == "{":
				bufplace = ""
				placestart = a+semistart+1
				while string[placestart] != "}":
					bufplace = bufplace + string[placestart]
					placestart +=1
				if string[placestart+1] == '*':
					poid = int(poid/int(string[placestart+2]))
				tabplace.append((bufplace,poid))
				nbplace += 1
		semistart = x+3
count = 0
finaltab = []
for place in tabplace:
	nbdouble = 0
	if place in tabplace:
		buftab = tabplace[:]
		smallerpoid = place[1]
		for c in range(tabplace.index(place), len(tabplace)):
			p = place[0]
			bufp = tabplace[c][0]
			if p == bufp:
				if smallerpoid > tabplace[c][1]:
					smallerpoid = tabplace[c][1]
				buftab.remove(tabplace[c])
		finaltab.append((place[0],smallerpoid))
	tabplace = buftab[:]
	count +=1

for x in range(0,len(finaltab)):
	print(finaltab[x])
