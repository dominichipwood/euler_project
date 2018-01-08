n=input("n=")
s1=0
for i in range(n+1):
    s1+=i
s1=s1**2
s2=0
for i in range(n+1):
    s2+=i**2
print(s1)
print(s2)
print(s1-s2)
