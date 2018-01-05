# python 3

from itertools import permutations
from functools import reduce
import euler_funcs as ef
primes=ef.primes(1000000)
bad_digits=[0,2,4,5,6,8]
for d in bad_digits:    # get rid primes with digits that do
    primes=list(filter(lambda x: str(d) not in str(x), primes))

def cycles(n):
    digits=list(str(n))
    N=len(digits)
    CoD=[[digits[-i+j] for j in range(N)] for i in range(1,N)] #cylces of digits
    # note i starts 1 as only need to check p in prime its non trival cylces
    return [int(reduce(lambda x,y : x+y, cycle)) for cycle in CoD]
counter=2
for p in primes:
    print(p)
    Bol=True
    for q in cycles(p):
        Bol=Bol and ef.is_prime(q)
    if Bol:
        counter+=1   
print("There are {} cycle primes less than {}".format(counter, 1000000))
    
    
    
            
        
        
        
    

