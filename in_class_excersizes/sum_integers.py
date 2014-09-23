#sums integers in range x to y

def sum_integer(x,y):
	sumo = x
	for i in range (x+1,y+1):
		sumo = sumo + i
		print i
	return sumo

print sum_integer(1,5)