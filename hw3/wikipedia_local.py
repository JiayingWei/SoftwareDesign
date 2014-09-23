#Creates a list of links connected to a chosen wikipedia link.

#takes an article and returns the first link on the page
def local_links(article, prev_article):
	from pattern.web import *
	w = Wikipedia()
	article = w.search(article)
	link =  article.links
	# print link
	if link[0] == article or link[0] == prev_article:
		# print 'in new link (inputs):'
		# print link[1] 
		# print article
		newlink = local_links(link[1], article)
		# print 'in new link (output):'
		# print newlink
		# print newlink[0]
		return newlink[0]
	else:	
		# print 'in link (output):'
		temp = str(link[0])
		# print 'after'
		print temp
		print ('hi' + temp)
		return 'hi'


def philosophy_game(origin):
	journey = [origin]
	while journey[-1] != 'Philosophy':
		if len(journey) == 1:
			journey.append(local_links(journey[-1],journey[-1]))
		else:
			journey.append(local_links(journey[-1],journey[-2]))
		print 'printing journey things:'
		print journey
		print 'printing input (-1 -2):'
		print journey[-1]
		print journey[-2]
	return journey

print local_links('Vatican City','Flag of Vatican City')
# if __name__ == '__main__':
# 	print philosophy_game('Vatican City')
