# a)
def filter_palindrom(l):
	return list(filter(lambda y: y if (y != y[::-1]) else "",l))

K = ["abba","aba", "abab", "ababa"] # ["abab"]

print(filter_palindrom(K))


# b)
def liste_kleiner(l1,l2):
	return list(map(lambda x,y: x if (x<=y) else y, l1, l2))

print(liste_kleiner([5,7,-3,-1], [2,10,-3,5])) # [2,7,-3,-1]


# c)
def custom_op(l):
	if type(l[0]) == int:
		for el in l:
			if type(el) != int:
				return lambda x: x
		return lambda x: x*2 
	elif type(l[0]) == str:
		for el in l:
			if type(el) != str:
				return lambda x: x
		return lambda x: x[::-1]
	return lambda x: x

L1 = [1,2,3] # [2,4,6]
L2 = ["ab","3a5",] # ["ba","5a3"]
L3 = [1,2,"ab"] # [1,2,"ab"]

print(list(map(custom_op(L1),L1)))
print(list(map(custom_op(L2),L2)))
print(list(map(custom_op(L3),L3)))


# d)

def sortiere(kleiner,L):
	trenner = 0
	while trenner != len(L):
		for i in range(trenner,len(L)):
			if kleiner(L[i],L[trenner]):
				L[trenner], L[i] = L[i], L[trenner]
		trenner += 1
	return L
 
kleiner = lambda w1,w2: (len(w1) == len(w2) and w1<w2) or (len(w1)<len(w2))

L = ["z","aaa","1","11111","ccv","22"]
print(sortiere(kleiner,L))