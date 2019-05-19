# Aufgabe 2
#
import random

class Intliste(object):

	def __init__(self,liste):
		self.liste = [x for x in liste if (type(x) == int)]

	def __len__(self):
		laenge = 0
		for x in self.liste:
			if type(x) == int:
				laenge += 1
		return laenge

	def __str__(self):
		l = 0
		for x in self.liste:
			if l <= len(str(x)):
				l = len(str(x))

		rs = "["
		k = 0
		for x in self.liste:
			rs += "0"*(l- len(str(x))) + str(x)
			k +=1
			if not k == len(self.liste):
				rs += ","
		return rs + "]"

	def __eq__(self,other):

		if not len(self.liste) == len(other.liste):
			return False

		for x in range(len(self.liste)):
			if not self.liste[x] == other.liste[x]:
				return False

		return True

	def __ne__(self,other):

		if not len(self.liste) == len(other.liste):
			return True

		for x in range(len(self.liste)):
			if not self.liste[x] == other.liste[x]:
				return True

		return False


	def __lt__(self,other):

		if len(self.liste) < len(other.liste):
			listee = len(self.liste)
		else:
			listee = len(other.liste)

		for x in range(listee):
			if not self.liste[x] == other.liste[x]:
				if self.liste[x] < other.liste[x]:
					return True
				else:
					return False

		if len(self.liste) < len(other.liste):
			return True	

		return False

	def __le__(self,other):

		if len(self.liste) < len(other.liste):
			listee = len(self.liste)
		else:
			listee = len(other.liste)

		for x in range(listee):
			if not self.liste[x] == other.liste[x]:
				if self.liste[x] < other.liste[x]:
					return True
				else:
					return False

		if len(self.liste) > len(other.liste):
			return False	

		return True

	def __gt__(self,other):
	
		if len(self.liste) > len(other.liste):
			listee = len(self.liste)
		else:
			listee = len(other.liste)

		for x in range(listee):
			if not self.liste[x] == other.liste[x]:
				if self.liste[x] > other.liste[x]:
					return True
				else:
					return False

		if len(self.liste) > len(other.liste):
			return True	

		return False

	def __ge__(self,other):

		if len(self.liste) > len(other.liste):
			listee = len(self.liste)
		else:
			listee = len(other.liste)

		for x in range(listee):
			if not self.liste[x] == other.liste[x]:
				if self.liste[x] > other.liste[x]:
					return True
				else:
					return False

		if len(self.liste) < len(other.liste):
			return False	

		return True

	def __add__(self,other):
		K = []
		for x in self.liste:
			K.append(x)
		for x in other.liste:
			K.append(x)
		return K

	def __sub__(self,other):
		for y in other.liste:
			for x, z in enumerate(self.liste):
				if z == y:
					self.liste[x] = []

		K = []
		for x in self.liste:
			if not type(x) == list:
				K.append(x)

		return K

#Nicht veraendern!
if __name__ == '__main__':
	# Sortiert Liste liste mittels Mergesort
	def mergesort(liste):

		if len(liste) < 2:
			return liste
	
		mitte = len(liste) // 2
		links = mergesort(liste[:mitte])
		rechts = mergesort(liste[mitte:])
		return merge(links,rechts)

	# mische aufsteigend sortierte Listen links und rechts zu einer aufsteigend sortierten Liste
	def merge(links, rechts):
		resultat = []
		i,j = 0,0

		while i < len(links) and j < len(rechts):
			if links[i] < rechts[j]:
				resultat.append(links[i])
				i += 1
			else:
				resultat.append(rechts[j])
				j += 1

		while i < len(links):
			resultat.append(links[i])
			i+= 1

		while j < len(rechts):
			resultat.append(rechts[j])
			j += 1

		return resultat



	n = 10
	m = 10
	r = 5
		
	# Ergebniskontrolle fuer Vergleiche
	# Erzeugt n Listen zufaelliger Laenge (von 0 bis m-1) mit zufaelligen Eintraegen (von 0 bis r-1). 


	Listen = [ Intliste([random.choice(range(r)) for j in range(random.choice(range(m)))]) for i in range(n) ]
	for liste in Listen:
		print(liste)

	Sortiert = mergesort(Listen)
	
	for liste in Sortiert:
		print(liste)

# Ihren globalen Testcode koennen Sie hier platzieren:

#L = Intliste([1,"ab",3,0.4])
#print(L)
