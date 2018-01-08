import functions
n=input("Smallest triangle number with more than n divisors for n=") 
m=1
a=0
divs=[]
while len(divs)<=n:
    a+=m
    divs=functions.divs(a)
    m+=1
print(a)
