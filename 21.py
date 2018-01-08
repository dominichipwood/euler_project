from functions import proper_divs
m=input("amicables under m=")
amici=[]
def d(n):
    return sum(proper_divs(n))
for a in range(m):
    b=d(a)
    if a!=b and d(b)==a:
        if  not a in amici:
            amici.append(a)
        if b not in amici and b<m:
            amici.append(b)
print(amici)
print(sum(amici))
