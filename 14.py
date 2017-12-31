n=input("n=")
lengths=[1]
starts=[1]	# start place : chain length
for t in range(2,n):
	print(t)	# so I know how fast its running
	s=t
	L=1
	while s!=1:	# Compute length of seq
		if s<t:
			L=L+lengths[s-1]-1
			break
		elif s%2==0:
			s=int(s/2)
			L+=1 
		else:
			s=3*s+1
			L+=1
	starts.append(t)
	lengths.append(L)	
Lmax=max(lengths)
smax=lengths.index(Lmax)+1
print("the maximum length of chain is "+str(Lmax))
print("the starting point is "+str(smax))


# a second attempt is a little quicker

lenghts=[0]+[1]*(n-1)
for t in range(1,n):
	s=t
	L=0
	while s!=1:
		if s<t:
			lenghts[t]=lengths[s]+L
			break
		elif s%2==0:
			s=int(s/2)
			L+=1 
		else:
			s=3*s+1
			L+=1
Lmax=max(lengths)
smax=lengths.index(Lmax)
print("the maximum length of chain is {}; the starting point is {}".format(Lmax,smax))	 



