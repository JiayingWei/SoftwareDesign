#Function returns true if string x is a palindrome

def is_palindrome(palindrome):
    forwards = palindrome.replace(" ","")
    forwards = forwards.lower()
    backwards = forwards.replace(" ","")[::-1]

    if forwards == backwards:
    	print 'lol palindrome'
    else:
    	print 'lol no'

is_palindrome('tracy no panic in a pony cart')