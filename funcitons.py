from math import sqrt
def prime(p):
	div=[]
	for i in range(2,int(sqrt(p))+1):
		if float(p)/float(i) % 1==0%1:
			div.append(i)
		if len(div)>0:
                    break
	return len(div)==0
def divs(n):
    divs=[]
    for i in range(1,int(sqrt(n))+1):
        if float(n)/float(i) % 1==0%1:
            divs.insert(int(len(divs)/2),i) # in accending order
            if float(i)!=float(n)/float(i):
                divs.insert(divs.index(i)+1,int(float(n)/float(i)))
    return divs
def proper_divs(n):
    divs=[1]
    for i in range(2,int(sqrt(n))+1):
        if float(n)/float(i) % 1==0%1:
            divs.insert(int(len(divs)/2)+1,i) # in accending order
            if float(i)!=float(n)/float(i):
                divs.insert(divs.index(i)+1,int(float(n)/float(i)))
    return divs
