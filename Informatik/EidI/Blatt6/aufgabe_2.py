# a)
def lies_ein():
	return [line[0:-1] for line in open("dictionary.txt","r")]

#print(lies_ein())


# b)
def buch_1(liste):
	return {i:len(i) for i in liste}

#print(buch_1(lies_ein()))


# c)
def buch_2():
	return { i+1: fib(i) for i in range(30)}

def fib(n):
	if n==0 or n==1:
		return 1
	else: 
		return fib(n-1)+fib(n-2)

#print(buch_2())


# d)
def fibonaccilaenge(wort, buch1, buch2):
	if wort in buch1:
		if buch1[wort] in buch2:
			return buch2[buch1[wort]]
	return None

#suche = input("Wort: ")
#print(fibonaccilaenge(suche,buch_1(lies_ein()),buch_2()))
print(fibonaccilaenge("Banane",buch_1(lies_ein()),buch_2()))