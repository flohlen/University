# c) nicht bearbeitet
# 	 bitte kuerzen ergänzen, um d) zutesten

#
# Aufgabe 2
#

def euklid(a,b):
	if a==0 or b==0:
		return "undefiniert"
	if a<b: return euklid(b,a)
	if a%b==0: 
		return b
	else: 
		return euklid(b,a%b)
		


class Bruch(object):

	def __init__(self, zaehler, nenner):
		self.set_bruch(zaehler,nenner)

	def __str__(self):
		return str(self.zaehler) + "/" + str(self.nenner)


	def __add__(self, other):
		oben = self.zaehler*other.nenner + self.nenner*other.zaehler
		unten = self.nenner*other.nenner
		return Bruch(oben, unten)


	def __sub__(self, other):
		oben = self.zaehler*other.nenner - self.nenner*other.zaehler
		unten = self.nenner*other.nenner
		return Bruch(oben, unten)


	def __float__(self):
		return self.zaehler/self.nenner


	def __mul__(self,other):
		oben = self.zaehler * other.zaehler
		unten = self.nenner * other.nenner
		return Bruch(oben,unten)

	def __truediv__(self,other):
		if other.zaehler == 0:
			raise ZeroDivisionError ("Es darf nicht durch 0 geteilt werden.")
		return self * other.umkehren()


	def umkehren(self):
		return Bruch(self.nenner, self.zaehler)		
			

	def set_bruch(self,zaehler,nenner):
		if nenner == 0:
			raise ValueError ("Nenner darf nicht 0 sein.")
		else:
			self.zaehler = zaehler
			self.nenner = nenner


	def kuerzen(self):
		return self

def rechne(b1_zaehler,b1_nenner,b2_zaehler,b2_nenner):
	b1 = Bruch(b1_zaehler,b1_nenner)
	b2 = Bruch(b2_zaehler,b2_nenner)
	try:
		k1 = b1+b2
		print(k1.kuerzen())

		k2 = b1-b2 
		print(k2.kuerzen())

		k3 = b1*b2
		print(k3.kuerzen())

		k4 = b1/b2
		print(k4.kuerzen())

	except ValueError:
		print("ValueError!")

	except ZeroDivisionError:
		print("ZeroDivisionError!")
	except:
		print("Probleme mit der Eingabe.")
		
	finally:
		print("Einen schönen Tag noch!")


# Nicht veraendern!
# if __name__ == '__main__':

# 	rechne(1,2,3,4)
# 	rechne(3,2,1,0)
# 	rechne(2,3,0,1)
# 	rechne(1,2,3,"vier")

# Ihren globalen Testcode koennen Sie hier platzieren:

L = Bruch(4,5)
print(L)
K = Bruch(0,1)
print(K)

print(K*L)
print(L/K) 
