#Cumulative Sum

original = [1,2,3]

def add_all(t):
	total = t
	for i in range(0,len(t)):
		if i == 0:
			total = total
		else:
			total[i] = total[i] + t[i-1]
   
	return total

print add_all(original)
