y = 1
eingabe = int(input("Bitte geben Sie eine ganze Zahl (>0) an:")) 
for i in range(1,eingabe+1):
    y = y*i
print("Ihre Eingabe: ",eingabe)
print("Davon ist die Fakultät: ",y)