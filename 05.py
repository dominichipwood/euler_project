def lcm(n,m):
       divsn=[]
       l=n*m
       for i in range(1,n+1):
           if float(n)/float(i) %1 ==0:
               divsn.append(i)
       for j in divsn:
            if float(m)/float(j) % 1==0:
                l=int(float(n*m)/float(j))
       return l
L=1
for k in range(1,21):
       L=lcm(k,L)
print(L)
       
