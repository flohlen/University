def find_pos(zeichenkette,zeichen):
	"""
	Position eines Zeichens in einer Zeichenkette
	"""
	for index, x in enumerate(zeichenkette):
		if zeichen == x:
			return index
	return -1

def find_line(eingabe):
	"""
	Postion eines Wortes in einem Wörterbuch
	"""
	file_dict = open("dictionary.txt","r")
	dictionary = file_dict.read()
	index = 0
	for x in dictionary.split("\n"):
		index+=1
		if eingabe == x:
			file_dict.close()
			return index
	file_dict.close()
	return -1

def build():
	"""
	Erstellung des Dictionary
	"""
	file_dict = open("dictionary.txt","w")
	file_original = open("de_DE_frami.dic","r")

	for x in file_original:
		# Leerzeile zwischen Kommentar und Wörterbuchinhalt mit "#" füllen
		if find_pos(x,"\n") == 0:
			x = "#"
		# Zeilen, die nicht "#" beinhalten bzw. beginnen von Anfang bis zum Trennstrich in das neue Wörterbuch schreiben
		if find_pos(x,"#") == -1:
			file_dict.write(x[0:find_pos(x,"/")] + "\n")

	file_dict.close()
	file_original.close()
	print("dictionary.txt erstellt.")

if input("Ist dictionary.txt bereits erstellt? (J/N)").lower() == "n":
	build()
else:
	eingabe = input("Wort: ")
	line = find_line(eingabe)
	if line == -1:
		print("Wort nicht gefunden.")
	elif line > -1:
		print("Zeile: ",line)
	else:
		print("Error")
