import re

def get_words_from_book(txtfilename):
	f = open(txtfilename,'r')
	fulltext = f.read()
	start = fulltext.find('www.gutenberg.net') + len('www.gutenberg.net')
	end = fulltext.find('End of Project Gutenberg')
	fulltext = fulltext[start:end]
	fulltext = fulltext.split(' ')
	words = fulltext.split('\n')
	
	wordbank = {}
	print words
	for word in words:
		if word.ifalpha() == True:
			if word not in wordbank.keys:
				wordbank[word] = 1
			else:
				wordbank[word] = wordbank[word] + 1
		else:
			word = word[:len(word)-1]
			if word not in wordbank.keys:
				wordbank[word] = 1
			else:
				wordbank[word] = wordbank[word] + 1

	print wordbank
get_words_from_book('the_tale_of_benjamin_button.txt')