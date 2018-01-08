from math import sqrt
n=input("primes less than n=")
primes=[2,3]
for p in range(5,n+1):
    divsp=[]
    for q in primes:
        divsp=[]
        if float(p)/float(q) % 1==0%1:
            divsp.append(q)
            break
        if q >int(sqrt(p)):
            break
    if len(divsp)==0:
        primes.append(p)
print(sum(primes))
    
        
