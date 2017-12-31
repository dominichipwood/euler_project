done before I realised sort function exists

import p022_names
names=p022_names.Names
alphabet=list("0ABCDEFGHIJKLMNOPQRSTUVWXYZ")
a1={ letter : alphabet.index(letter) for letter in alphabet} # letter to its number
while names!=[]:
	m=min(names)
	names1.append(m)
	names.remove(m)
names=names1
print(names)
def name_score(name):
	s1=0
	for letter in name:
		s1+=a1[letter]	# compute sum of letter numbers	
	return s1*(1+names.index(name)) #multiply by its place
N=0
for name in names:
	print(name)
	N+=name_score(name)
print(N)
