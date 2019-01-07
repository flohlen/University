def programm2(n):  # Eingabegroesse: n
	i = 0
	while i <= n:
		i += 1
		if i ** 2 > 0:
			break
	return i

print(programm2(-1))

def programm1(n):  # Eingabegroesse: n
	if n < 2:
		return False
	divisor = 2
	while divisor * 2 < n:
		divisor += 1
		if n % divisor == 0:
			return False
	return True

print(programm1(96))

def programm4(n):  # Eingabegroesse: n
	i = 1
	for j in range(n):
		i *= 2
	j = 1
	for k in range(i):
		k *= 2
	return k

print(programm4(10))