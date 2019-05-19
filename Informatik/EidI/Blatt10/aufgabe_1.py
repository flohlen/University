class Mensch(object):
	
	def __init__(self, name, weiblich):
		self.name = name
		self.weiblich = weiblich

	def get_name(self):
		return self.name	

	def get_weiblich(self):
		return self.weiblich

	def set_name(self, neuername):
		self.name = neuername
		if type(self) == Gallier:
			if self.get_weiblich():
				if len(neuername) >= 4:
					if not (neuername[-1] == "e" and neuername[-2] == "n" and neuername[-3] == "i"):
						self.name = neuername + "ine"
			else:
				if len(neuername) >= 3:
					if not (neuername[-1] == "x" and neuername[-2] == "i"):
						self.name = neuername + "ix"

		elif type(self) == Roemer:
			if self.get_weiblich():
				if len(neuername) >= 4:
					if not (neuername[-1] == "a"):
						self.name = neuername + "a" 
			else:
				if len(neuername) >= 3:
					if not (neuername[-1] == "s" and neuername[-2] == "u"):
						self.name = neuername + "us"

class Gallier(Mensch):

	def __init__(self,name,weiblich,wildschweine = 0):
		Mensch.__init__(self,name,weiblich)
		self.set_name(name)
		self.wildschweine = wildschweine

	def get_wildschweine(self):
		return self.wildschweine

	def iss_wildschweine(self):
		self.wildschweine += 1

class Roemer(Mensch):
	imperator = ""

	def __init__(self,name,weiblich,verloren = 0):
		Mensch.__init__(self,name,weiblich)
		self.set_name(name)
		self.verloren = verloren
		if Roemer.imperator == "":
			Roemer.imperator = self

	def verliere(self):
		self.verloren += 1

	def wie_oft_verloren(self):
		return self.verloren

	def werde_imperator(self):
		Roemer.imperator = self

class Dorf(object):

	def __init__(self,bewohner,druide,barde):
		self.bewohner = bewohner
		self.druide = druide
		self.barde = barde

	def get_bewohner(self):
		return self.bewohner

	def get_druide(self):
		return self.druide

	def set_druide(self,name):
		self.druide = name

	def get_barde(self):
		return self.barde

	def set_barde(self,name):
		self.barde = name

class Legion(object):

	def __init__(self,soldaten,zenturio):

		self.zenturio = zenturio
		
		ss = []
		for x in soldaten:
			if not (x.get_weiblich() or x == zenturio):
				ss.append(x)
		self.soldaten = set(ss)
		
	def get_zenturio(self):
		return self.zenturio

	def set_zenturion(self):
		self.zenturio = zenturio

	def rekrutiere(self,ein_roemer):
		if not (ein_roemer.get_weiblich() or ein_roemer == self.get_zenturio()):
			self.soldaten.add(ein_roemer)

	def pensioniere(self,ein_roemer):
		self.soldaten.discard(ein_roemer)

def wettkampf(ein_dorf,eine_legion):

	gallianten_od = []
	for x in ein_dorf.get_bewohner():
		if not x == ein_dorf.get_druide():
			gallianten_od.append(x)

	gallianten_ob = []
	for x in ein_dorf.get_bewohner():
		if not x == ein_dorf.get_barde():
			gallianten_ob.append(x)

	roermoer = [eine_legion.get_zenturio()]
	for x in eine_legion.soldaten:
		roermoer.append(x)

	for x in roermoer:
		for y in gallianten_od:
			print("Gallier " + y.get_name() + " misst sich mit Roemer/Zenturio " + x.get_name())
			x.verliere()
			break

	for x in gallianten_ob:
		x.iss_wildschweine()


# Nicht veraendern!
if __name__ == '__main__':

# Loesen Sie Aufgabenteil g) hier:
	Laureline = Gallier("Laurel",True)
	Canine = Gallier("Canine",True)
	Apfelsine = Gallier("Apfelsine",True)

	Praefix = Gallier("Praefix",False)
	Infix = Gallier("Infix",False)
	Postfix = Gallier("Postf",False)

	Salta = Roemer("Salt",True)
	Mendoza = Roemer("Mendoza",True)
	Ushuaia = Roemer("Ushuaia",True)

	Primus = Roemer("Primus",False)
	Secundus = Roemer("Secundus",False)
	Tertius = Roemer("Tertius",False)
	Quartus = Roemer("Quartus",False)
	Quintus = Roemer("Quint",False)

	Oelixdorf = Dorf({Laureline,Apfelsine,Praefix},Laureline,Praefix)
	Bekdorf = Dorf({Laureline,Postfix,Infix,Canine},Infix,Canine)

	Hispana = Legion({Salta,Quintus,Quartus,Tertius,Mendoza},Salta)
	

# Diesen Teil duerfen Sie nicht veraendern

	if not (Laureline.get_name() == "Laureline" and Canine.get_name() == "Canine"):
		print("Fehler: Gallierinnen falsch benannt")

	if not (Praefix.get_name() == "Praefix"  and Postfix.get_name() == "Postfix" ):
		print("Fehler: Gallier falsch benannt")

	if not (Salta.get_name() == "Salta" and Ushuaia.get_name() == "Ushuaia"):
		print("Fehler: Roemerinnen falsch benannt")

	if not (Primus.get_name() == "Primus" and Quintus.get_name() == "Quintus"):
		print("Fehler: Roemer falsch benannt")

	if not (Roemer.imperator == Salta):
		print("Fehler: Imperator falsch")
	
	Primus.werde_imperator()

	if not Roemer.imperator == Primus:
		print("Fehler: Thronfolge kaputt")


	Laureline.set_name("Geraldine")
	Canine.set_name("Paul")
	Praefix.set_name("Unix")
	Infix.set_name("Append")
	Mendoza.set_name("Catamarca")
	Ushuaia.set_name("Viedm")
	Primus.set_name("Airbus")
	Secundus.set_name("Autob")

	if not (Laureline.get_name() == "Geraldine" and Canine.get_name() == "Pauline" and Praefix.get_name() == "Unix" and Infix.get_name() == "Appendix" and Mendoza.get_name() == "Catamarca" and Ushuaia.get_name() == "Viedma" and Primus.get_name() == "Airbus"  and Secundus.get_name() == "Autobus" ):
		print("Fehler: Namensaenderung funktioniert nicht korrekt")


	Laureline.set_name("Laureline")
	Canine.set_name("Canine")
	Praefix.set_name("Praefix")
	Infix.set_name("Infix")
	Mendoza.set_name("Mendoza")
	Ushuaia.set_name("Ushuaia")
	Primus.set_name("Primus")
	Secundus.set_name("Secundus")
	
	if not (Oelixdorf.get_barde() == Praefix and Oelixdorf.get_druide() == Laureline and Oelixdorf.get_bewohner() == {Apfelsine, Praefix, Laureline} ):
		print("Fehler: Dorf falsch erstellt")

	if not (Bekdorf.get_barde() == Canine and Bekdorf.get_druide() == Infix and Bekdorf.get_bewohner() == {Laureline, Postfix, Infix, Canine} ):
		print("Fehler: Dorf falsch erstellt")

	if not (Hispana.get_zenturio() == Salta and Hispana.soldaten == {Quintus, Quartus, Tertius} ):
		print("Fehler: Legion falsch")


	Hispana.rekrutiere(Secundus)
	Hispana.rekrutiere(Ushuaia)	
	Hispana.pensioniere(Tertius)
	Hispana.pensioniere(Tertius)
	Hispana.rekrutiere(Salta)
	
	if not (Hispana.soldaten == {Secundus, Quartus, Quintus}):
		print("Fehler: Legion arbeitet falsch")


	wettkampf(Oelixdorf, Hispana)

	if not ((Secundus.wie_oft_verloren() == 1) and (Salta.wie_oft_verloren() == 1) and (Laureline.get_wildschweine() == 1) and (Canine.get_wildschweine() == 0)):
		print("Fehler: Wettkampf funktioniert nicht")
	
	Bekdorf.set_barde(Laureline)
	Hispana.rekrutiere(Primus)
	wettkampf(Bekdorf, Hispana)
	if not (Secundus.wie_oft_verloren() == 2 and Primus.wie_oft_verloren() == 1 and Laureline.get_wildschweine() == 1 and Canine.get_wildschweine() == 1):
		print("Fehler: Wettkampf funktioniert nicht richtig")


# Ihre Ausgabe soll in etwa folgendes Format haben:
# Gallier Apfelsine misst sich mit Roemer Quintus.
# Gallier Praefix misst sich mit Roemer Quartus.
# Gallier Apfelsine misst sich mit Roemer Secundus.
# Gallier Praefix misst sich mit Zenturio Salta.
# Gallier Laureline misst sich mit Roemer Primus.
# Gallier Postfix misst sich mit Roemer Secundus.
# Gallier Canine misst sich mit Roemer Quartus.
# Gallier Laureline misst sich mit Roemer Quintus.
# Gallier Postfix misst sich mit Zenturio Salta.
