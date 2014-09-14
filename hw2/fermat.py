def check_fermat(a,b,c,n):
	if a**n + b**n == c**n:
		print 'Holy smokes, Fermat was wrong!'
        else:
    	    print "No, that doesn't work. Thank you for participating in our program"

def input_fermat():
    print "Hello, in an effort to disprove Fermat's Last Theorum, we have randomly selected people from the civilian population to disprove the theorum. We will not provide any additional context."
    a = int(raw_input('Enter a number for variable a: '))
    b = int(raw_input('Enter a number for variable b: '))
    c = int(raw_input('Enter a number for variable c: '))
    n = int(raw_input('Enter a number for variable n: '))

    check_fermat(a,b,c,n)

input_fermat()