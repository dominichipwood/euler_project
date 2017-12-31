#soln on python 2

def is_pan(n):
	s=str(n)
	return s==s[::-1] 	# s[::-1] reverse string

panodigits=[i for i in range(1000000) if is_pan(i)]

def is_bpan(n):
	bs=str(bin(n))[2:]
	return bs==bs[::-1]

doublepanos=[i for i in panodigits if is_bpan(i)] #only check on already 1 panodigital numbers

print(sum(doublepanos))
