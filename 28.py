N=input("size of square?")
# This can be done looking at it can see is  . . . .
s=1
for n in range(1,int((N+1)/2)):
	m=2*n+1
	s=s+4*m**2 - 6*(m-1)
print(s)
