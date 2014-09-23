#Returns factorial of n

def factorial(n):
	total = n
	for i in range(1,n-1):
		total = total*(n-i)

	return total

print factorial(5)