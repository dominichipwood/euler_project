import euler_functions as ef
primes=list(ef.primes(1000000))	#primes meno di 100000

def B(n):	#does it contains digit 0,4,6 or 8
	B= "4" in str(n) or "6" in str(n) or "8" in str(n) or "0" in str(n)
	return B
primes=[p for p in primes if not B(p)]	# gid rid of those primes without hope
def Ltruncated(n):
	if n in {2,3,5,7}:
		return True
	elif n in {0,1,4,6,8}:
		return False
	else:
		n1=str(n)[1:]
		n1=int(n1)
		return n1 in primes and Ltruncated(n1)

def Rtruncated(n):
	if n in {2,3,5,7}:
		return True
	elif n in {0,1,4,6,8,9}:
		return False
	else:
		n1=str(n)[:-1]
		n1=int(n1)
		return n in primes and Rtruncated(n1)

trunc_primes=[p for p in primes if Ltruncated(p) and Rtruncated(p)]
trunc_primes.remove(2)
trunc_primes.remove(3)
trunc_primes.remove(5)
trunc_primes.remove(7)
print(trunc_primes)
print(len(trunc_primes))
