# problem 14 solved on python 2. Tested for small triangle before solving on bigger triangle

tri=[
[3],
[7,4],
[2,4,6],
[8,5,9,3]]

def path_sum(p):
	if p>=0 and p<=7:
		s=3	# subtotal
		x=0	# x coordinate
		path1=list(str(bin(p)))[2:]
		print(path1)
		path=["0"]*3		# make sure length 8
		for i in range(len(path1)):	
			path[i]=path1[len(path1)-1-i]
		print(path)
		for y in range(3):	# work way down triangle
			x+=int(path[y])
			s+=tri[y+1][x]
		return s
	else: raise ValueError
Tri=[
[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 04, 82, 47, 65],
[19, 01, 23, 75, 03, 34],
[88, 02, 77, 73, 07, 63, 67],
[99, 65, 04, 28, 06, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23]]

def Path_Sum(p):
	if p>=0 and p<=2**14:
		s=75	# s=subtotal
		x=0	# x coordinate
		path1=list(str(bin(p)))[2:]
		path=["0"]*14		# make sure length 14
		for i in range(len(path1)):	
			path[i]=path1[len(path1)-1-i]
		for y in range(14):	# work way down triangle
			x+=int(path[y])
			s+=Tri[y+1][x]
		return s
	else: raise ValueError
Smax=0
for p in range(2**14):
	Smax=max(Smax,Path_Sum(p))
print(Smax)
