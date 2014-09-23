#Returns True if n is a prime number

def is_prime(n):
	for i in range(1,n+1):
		if n % i == 0 and i != 1 and i != n:
			print 'not prime'
			break

		if i == n:
			print 'prime'
			break

is_prime(593)