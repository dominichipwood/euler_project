def s5pd(n):    #sum of 5th powers of digits
    digits=[int(t) for t in list(str(n))]
    return sum(d**5 for d in digits)
nums=[]
n=2
for n in range(2,1000000):
    if s5pd(n)==n:
        nums.append(n)
print(nums)
print(sum(nums))
    
    
