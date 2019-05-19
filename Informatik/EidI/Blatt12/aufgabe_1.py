from tkinter import *
import random



class Figur(object):
	
	def __init__(self,farbe):
		self.farbe = farbe
		
		
	def zeichnen(self,canvas,x,y):
		# Platzhalter fuer Verhalten, welches von Unterklassen implementiert werden soll
		raise NotImplementedError()
		

######### Fügen Sie hier die benötigten Klassen ein. ######

class Rechteck(Figur):
	def __init__(self,farbe,a,b):
		self.farbe = farbe
		self.seite_a = a
		self.seite_b = b

	def zeichnen(self,canvas,x,y):
		canvas.create_rectangle(x,y,x+self.seite_a,y+self.seite_b,fill=self.farbe)

class Kreis(Figur):
	def __init__(self,farbe,r):
		self.farbe = farbe
		self.radius = r

	def zeichnen(self,canvas,x,y):
		canvas.create_oval(x-(self.radius/2),y-(self.radius/2),x+(self.radius/2),y+(self.radius/2),fill=self.farbe)

class Zusammengesetzt(Figur):
	def __init__(self,figurenliste):
		self.figurenliste = figurenliste

	def zeichnen(self,canvas,x,y):
		for fig in self.figurenliste:
			fig[0].zeichnen(canvas,x+fig[1],y+fig[2])


###########################################################
		
			



master = Tk()
master.title("Mein Wald")
canvas_width = 1000
canvas_height = 800

w = Canvas(master, width=canvas_width, height=canvas_height)              # der Name des Leinwandobjekts ist also w

w.pack()
master.update()





######### Fügen Sie hier ihren Testcode ein um den Wald zu zeichnen. ###########

# Stamm
R = Rechteck("brown",16,100)

# Baumkrone
K = Kreis("green",100)

# Anzahl der Baeume
baum_anz = 200

# Relationen zwischen Stamm und Baumkrone
# Damit der Stamm mittig unter der Baumkrone liegt
relations_r_1 = -8
relations_r_2 = 30

L = []
for x in range(baum_anz):
	# Zufaellige Werte um den Leinwandmittelpunkt 
	val_1 = random.randint(-(canvas_width/2), canvas_width/2)
	val_2 = random.randint(-(canvas_height/2), canvas_height/2)
	
	L.append((R,val_1+relations_r_1,val_2+relations_r_2))
	L.append((K,val_1,val_2))

W = Zusammengesetzt(L)
# Wald ausgehend vom Leinwandmittelpnkt zeichnen
W.zeichnen(w,canvas_width/2,canvas_height/2)

################################################################################

mainloop()