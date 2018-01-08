from math import sqrt
def f(p):
	div=[]
	for x in range(2,int(sqrt(p))+1):
		if float(p)/float(x) % 1==0%1:
			div.append(x)
		if len(div)>0:
                    break
	return len(div)==0
n=input("nth prime for n=")
primes=[]
i=2
while len(primes)<n:
    for p in primes:
        if i<=int(sqrt(p)) or i% p==0%p:
            i+=1
    if f(i):
        primes.append(i)
    i+=1
print(primes[n-1])
