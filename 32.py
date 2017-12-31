from itertools import permutations
from math import sqrt
def t2n(T):	#tuple to number
	s=reduce(lambda x,y: str(x)+str(y), T)
	return int(s)
def pan9(a,b,c):
	abc=str(a)+str(b)+str(c)
	return set(list(abc))=={"1","2","3","4","5","6","7","8","9"}
pans=[]		#panidigital numbers
for i in range(1,10):
	pans=pans+list(permutations([1,2,3,4,5,6,7,8,9],i))
pans=[t2n(pan) for pan in pans]
print(len(pans))
def panprod(p):		# does it have a pan product
	for d in range(2,int(sqrt(p))):
		if p%d==0:
			digits=str(d)+str(int(p/d))+str(p)
			if "".join(sorted(digits))=="123456789":
				return True
	return False
pan_prods=[]
for p in pans:
	if p>10000:
		break
	if panprod(p):
		pan_prods.append(p)
print(pan_prods)

	
