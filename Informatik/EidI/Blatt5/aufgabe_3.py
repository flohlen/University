#n = int(input("Groesse des Schachbretts: "))

#pos = int(input("Springerposition Zeile: ")),int(input("Springerposition Reihe: "))


n = 4
pos = (2,2)

brett = [[0 if (i == pos[0] and j == pos[1]) else -1 for j in range(n)] for i in range(n)]

#print(brett)

def possible_moves(sp,n):
	zug_liste = []
	for i in range(-2,2+1):
		for j in range(-2,2+1):
			if abs(i) != abs(j) and not (j==0 or i == 0):
				if ((sp[0]+i)>=0 and (sp[0]+i<=n-1)) and ((sp[1]+j)>=0 and (sp[1]+j)<=n-1):
					zug_liste.append((sp[0]+i,sp[1]+j))
	return zug_liste

print(possible_moves(pos,len(brett)))

# def min_moves(brett,sp,n):
# 	for m in possible_moves(sp,n):
# 		if brett[m[0]][m[1]] == -1:
# 			brett[m[0]][m[1]] == 1:
# 			min_moves(brett,m,n)

sprung_buch = {}

def min_moves(brett,sp,n):
	if sp not in sprung_buch:

		if brett[sp[0]][sp[1]] == 0:
			sprung_buch[sp] = 0
		else:
			sprung_buch[sp] = 1
			brett[sp[0]][sp[1]] = 1

		for m in possible_moves(sp,len(brett)):
			min_moves(brett,sp,n+1)
	
	else:

		for m in possible_moves(sp,len(brett)):
			if brett[m[0]][m[1]] < n:
				




	# for m in possible_moves(sp,n):
	# 	if min_moves(brett,m,n):

	# 		if brett[m[0]][m[1]] < sprung_buch[sp]:

	# 			if brett[m[0]][m[1]] == -1:
	# 				brett[m[0]][m[1]] = 1
	# 			else:
	# 				#brett[m[0]][m[1]] += 1
	# 				print("nix")
	# 			print(brett)
	# 			min_moves(brett,m,n)

	

		#if brett[sp[0]][sp[1]] <= brett[m[0]][m[1]]:
		#	break


#print(min_moves(brett,pos,n))

# if min_moves(brett,m,n) > n or min_moves(brett,m,n) == 0:
# 			return n
# 		else:
# 			if brett[sp[0]][sp[1]] == -1:
# 				brett[sp[0]][sp[1]] == 1
# 				min_moves(brett,m,n)
# 			else:
# 				brett[sp[0]][sp[1]] += 1