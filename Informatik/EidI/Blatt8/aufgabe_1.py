# Aufgabe 1
#

def bisection2(L,e): # Diese Zeile duerfen Sie nicht veraendern
	def bisection_hilfe(L, e, links, rechts):

		if links >= rechts:
			if (links == rechts and L[links] == e):
				return links
			else:
				return -1

		mitte = (links + rechts) // 2

		if L[mitte] == e:
			return mitte
		elif L[mitte] > e:
			return bisection_hilfe(L,e,links,mitte-1)
		else:
			return bisection_hilfe(L,e,mitte+1,rechts)

	if len(L) == 0:
		return -1
	else:
		return bisection_hilfe(L,e,0,len(L)-1)

# Nicht veraendern!
if __name__ == '__main__':
# Ihren globalen Testcode koennen Sie hier platzieren:
	L = (0,1,2,3,4,5,6,7,8,9,10)
	print(bisection2(L,4))

	K = ("a","b","c","d","e")
	print(bisection2(K,"c"))