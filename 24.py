
n=input("the nth lenxicographic permutation for n=")
def fact(p):    # n! function
	m=1
	for k in range(1,p+1):
		m*=k
	return m




dig_pos=[]   #the 0th digit is dig_pos[0]th of [0,1,. . ,9], the 1st digit is dig_pos[1] of [0,1, . . ,9]\ [0th digit], etc. 
for t in range(9,0,-1): #There are 10 steps as 10! permutations.
    i=0
    while i*fact(t)<n:   #There are 9! that start with 0, 9! that start with 1, . . ., where does n fit?
        i+=1
    dig_pos.append(i-1)
    n=n-(i-1)*fact(t)
dig_pos.append(0)     # at 10th digit only 1 possibility left = 0
nums=[0,1,2,3,4,5,6,7,8,9]
p=[]    # p is the desired permutation as list of single digit
for pos in dig_pos:
    p.append(str(nums[pos]))
    nums.remove(nums[pos])
perm=" "
for sigma in p:
    perm=perm+sigma
print(perm)
