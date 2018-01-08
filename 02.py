lista=[1,2]
x=2
while x<=4000000:
    n=len(lista)
    x=lista[n-2]+lista[n-1]
    lista.append(x)
n=len(lista)
lista=lista[0:n-1]
n=len(lista)
lista2=[]
for i in range(0,n):
    if (lista[i]%2==0%2):
        lista2.append(lista[i])
print(lista2)
print(sum(lista2))
