lista1=list(range(0,1000,3))
lista2=list(range(0,1000,5))
lista = lista1+lista2
x=0
y=0
while x<1000:
    if x in lista:
        y=y+x
    x=x+1
print(y)
