# solved on python 2

n=input("largest prime factor of n=")
print(str(n)+"? Lo so!")
from math import sqrt
def f(p):
	div=[]
	for i in range(2,int(sqrt(p)+1)):
		if float(p)/float(i) % 1 ==0%1:
			div.append(i)
		if len(div)>0:
			break
	return len(div)==0
print(f(n))
j=2
while j <= int(sqrt(n)):
	if float(n)/float(j) % 1 ==0%1:
		n=int(float(n)/float(j))
	else: j=j+1
print(n)
