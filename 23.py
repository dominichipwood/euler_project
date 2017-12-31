# this first attempt runs too slow, 23_1.py is quicker but looked at someone else solution for it

import euler_functions as ef
from math import sqrt
m=input("abundants less than m=")
def is_abun(n): 	# is n abundant
	s=0
	for d in range(2,int(sqrt(n))+1):
		if s>n:
			break
		elif float(n) % float(d) ==0:
			s+=d
			if d != int(n/d):
				s+=int(n/d)
	return s>n 
def abundants(n):	# list abundants less than n
	nums=list(range(1,n))
	abuns=[]
	i=0
	j=1
	while i<len(nums):
		if is_abun(nums[i]):
			for j in range(1,int(n/nums[i])+1):
				abuns.append(nums[i]*j)
			for j in range(1,int(n/nums[i])+1,nums[i]):
				if nums[i]*j in nums: 
					nums.remove(nums[i]*j)
		else: i+=1
	return abuns
abuns=abundants(m)
so2a=[]
for n in range(m):	#check which numbers sum of 2 abundant nums
	for a in abuns:	# for each abund < n check n-a is abun
		if a>n/2:
			break
		elif n-a in abuns:	
			so2a.append(n)
			break
# runs to slow, try sieving out stuff. I think a abundant implies na abundant for all n
for n in so2a:
	if not is_abun(n):
		print(n)
		
