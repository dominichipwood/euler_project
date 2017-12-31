import euler_functions as ef
from itertools import product
n=input("mod a b less than n=")
primes=ef.primes(10000)
B=ef.primes(n)	# list of possible b values
		# note B should inculde -p if -p is considered 				prime	
A=list(range(-n+1,n))
AxB=ef.product(A,B)
primes=set(primes)
def q(a,b,n):
	return n**2+a*n+b
def mult((a,b)):
	return a*b

def lcpq((a,b)):	# len of chain of primes of quadratic q
	n=1
	while q(a,b,n) in primes:
		n+=1
	return n
PAIR=(0,0)
L=0
for pair in AxB:
	l=lcpq(pair) 
	if l>L:
		L=l
		PAIR=pair
print([PAIR, mult(PAIR), L])



