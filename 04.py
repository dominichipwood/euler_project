#problem 4 soved in python 2

from math import log10
def Pal(n):	
	k=1
	while k<=n:
		k*=10
	k=int(log10(k))
	digits=[]
	for i in range(1,k+1): 
		d=(n% (10**i))/10**(i-1)
		n=n-d*10**(i-1)
		digits.append(d)
	t=len(digits)
	P=(digits[0]==digits[t-1])
	for j in range(t):
		P=P and digits[j]==digits[t-1-j]
		if P==False:
			break
	return P
p=0
for i in range(100,1000):
	for j in range(i,1000):
		if Pal(i*j) and i*j > p:
			p=i*j
			i0=i
			j0=j
print(p)
print(i0)
print(j0)
