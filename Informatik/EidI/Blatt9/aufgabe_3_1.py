# Aufgabe 3
#

import random
import time



def merge(links, rechts):
	global vergleiche
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


def mergesort(liste):
	if len(liste) < 2:
		return liste
	
	mitte = len(liste) // 2
	links = mergesort(liste[:mitte])
	rechts = mergesort(liste[mitte:])
	return merge(links,rechts)


def bubblesort(liste):
	for i in range(len(liste)):
		sortiert = True
		for j in range(0,len(liste)-i-1):
			if liste[j] > liste[j+1]:
				liste[j], liste[j+1] = liste[j+1], liste[j]
				sortiert = False
		if sortiert:
			break
	return liste

def qsort(liste):  
	global vergleiche
	linke=[]
	rechte=[]
	if len(liste) <= 1:
		return liste

	pivot = 0 

	for i in range(len(liste)):
		if i!= pivot:
			if liste[i] < liste[pivot]:
				linke.append(liste[i])
			else:
				rechte.append(liste[i])

	return qsort(linke)+liste[pivot:pivot+1]+qsort(rechte)


# Implementieren Sie diese Funktion
def radixsort(liste, stelligkeit, tiefe):

	if len(liste) <= 1 or stelligkeit > tiefe:
		return liste

	L = [list() for x in range(10)]

	for x in liste: 
		L[int(str(x)[stelligkeit])].append(x)

	K = []
	for x in range(10):
		K += radixsort(L[x],stelligkeit+1,tiefe)

	return K

# Nicht veraendern!
if __name__ == '__main__':

	def test(s,p,t):
		#s = 8  # Veraendern Sie diese drei Werte fuer Aufgabenteil b) 
		#p = 5  #
		#t = 5  #

		liste = random.sample(range(10 ** s, 10 ** (s +1)  ), 10 ** p)
		kopie = liste[:]
		kopie2 = liste[:]

		t0 = time.process_time()
		liste = radixsort(liste, 0, t-1)
		liste = bubblesort(liste)
		t1 = time.process_time() - t0
		rbs = t1
		#print(f"Radixsort + Bubblesort: {t1} Sekunden")

		t0 = time.process_time()
		kopie = mergesort(kopie)
		t1 = time.process_time() - t0
		ms = t1
		#print(f"Mergesort: {t1} Sekunden")

		t0 = time.process_time()
		kopie2 = qsort(kopie2)
		t1 = time.process_time() - t0
		qs = t1
		#print(f"Quicksort: {t1} Sekunden \n")

		return [rbs,ms,qs]

fil = open("a3.txt","w")
L = []
for s in range(10):
	for p in range(1,5):
		for t in range(1,s):
			try:
				avg = [0,0,0]
				for x in range(10):
					testv = test(s,p,t)
					avg[0] += testv[0]
					avg[1] += testv[1]
					avg[2] += testv[2]

				avg[0] = avg[0]/10
				avg[1] = avg[1]/10
				avg[2] = avg[2]/10

				print(s,p,t,avg[0],avg[1],avg[2])

				fil.write(str(s) + " " + str(p) + " " + str(t) + " " + str((str(round(((avg[1]/avg[0])-1)*100,5)) + "%", str(round(((avg[2]/avg[0])-1)*100,5)) + "%")) + "\n")
			except:
				v = 1
# avg = [0,0,0]
# s = 7
# p = 5
# t = 5
# for x in range(10):
# 	testv = test(s,p,t)
# 	avg[0] += testv[0]
# 	avg[1] += testv[1]
# 	avg[2] += testv[2]

# avg[0] = avg[0]/10
# avg[1] = avg[1]/10
# avg[2] = avg[2]/10

# print(s,p,t,avg[0],avg[1],avg[2])

# fil.write((str(s) + str(p) + str(t) + str((str(round(((avg[1]/avg[0])-1)*100,5)) + "%", str(round(((avg[2]/avg[0])-1)*100,5)) + "%"))) + "\n")


fil.close()

# Ihren globalen Testcode koennen Sie hier platzieren: