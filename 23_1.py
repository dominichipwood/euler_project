# an imporved solution to problem 23, done having looked at other online solutions

N=28123
sod=[0]*N	#sod[n] will be sum of proper divisors 
for d in range(1,N): 
	for i in range(2*d,N,d):    #2*i restricts to proper divs 
		sod[i]+=d	 #i is a proper divisor for each j
abuns=[n for n in range(N) if sod[n]>n]
so2a=[]
for n in range(N):
	for a in abuns:
		if a>n:
			break
		elif sod[n-a]>n-a:
			so2a.append(n)
			break
nso2a=[n for n in range(N) if not n in so2a]
print(sum(nso2a))
