# some common funcitons for solving problems

from math import sqrt
def prop_divs(n):
	divs=[]
	for d in range(2,int(sqrt(n))+1):
		if float(n) % float(d) ==0:
			divs.append(d)
			if d != int(n/d):
				divs.append(int(n/d))
	return [1]+sorted(divs)	
def all_divs(n):
	divs=[]
	for d in range(2,int(sqrt(n))+1):
		if float(n) % float(d) ==0:
			divs.append(d)
			divs.append(int(n/d))
	return sorted(divs)
def primes1(n):	#this, my 1st prime sieve is slower, i think because remove takes more time as reproduces list each time
	primes=list(range(3,n,2))
	i=0
	while i < len(primes):
		print(i)
		p=primes[i]
		for q in primes[i:]:
			if p*q>primes[-1]:
				break
			primes.remove(p*q)
		i=i+1
	return [2]+primes

	
def primes(n):
	isprime=[False]+[False]+[True]*(n-2)
	for i in range(2,int(sqrt(n))+1):
		print(i)
		for j in range(i*i,n,i):
			isprime[j]=False
	return [p for p in range(n) if isprime[p]]
	
primes(10000000)
print("primes fatto")

def product(L,K):
	LxK=[]
	for x in L:
		for y in K:
			LxK.append((x,y))
	return LxK
