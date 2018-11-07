def bin_rek_search(w,e,lg,rg):
	"""
	Errechnung der Kubikwurzel von w mit einer Fehlertoleranz von weniger gleich e im Intervall von lg bis rg
	"""
	# Mittelwert bilden	
	mw = (lg+rg)/2.0
	# rechte Grenze kann nicht groesser als linke Grenze sein
	if rg < lg:
		return "Error"
	# Wenn der Abstand zwischen der Kubik des Mittelwerts und der eingegebenen Zahl kleiner gleich der Fehlertoleranz ist
	if abs(mw**3-w)<=e:
		return mw
	else:
		# Wenn die Kubik des Mittelwertes kleiner als die Eingegebene Zahl ist, dann ist der Suchintervall: [mw:rg]
		# Wenn nicht, dann ist der Suchintervall [lg:mw]
		if mw**3<w:
			lg=mw
		else:
			rg=mw
		# Rekursiver Funktionsaufruf
		return bin_rek_search(w,e,lg,rg)

w = float(input("Zahl: "))
epsilon = float(input("Fehlertoleranz >0: "))

if epsilon > 0 :
	if w>0:
		print("Durch rekursive Binäresuche angenäherte Kubikwurzel mit einer Fehlertoleranz von weniger-gleich",epsilon,":",bin_rek_search(w,epsilon,0,w))
		print("Durch Termumformung angenäherte Kubikwurzel: [Zahl**(1/3)]", w**(1/3))
	elif w<0:
		w = abs(w)
		print("Durch rekursive Binäresuche angenäherte Kubikwurzel mit einer Fehlertoleranz von weniger-gleich",epsilon,": -",bin_rek_search(w,epsilon,0,w))
		print("Durch Termumformung angenäherte Kubikwurzel: [Zahl**(1/3)]: -", w**(1/3))
	else:
		print("Fehler: Zahl darf nicht 0 sein.")
else:
	print("Fehler: Epsilon soll groesser als 0 sein.")