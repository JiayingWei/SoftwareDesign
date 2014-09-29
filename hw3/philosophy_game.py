#plays the wikipedia philosophy game - clicks the first link on every page until it reaches philosophy. This program does cheat in the sense that it will click the first unvisited link rather than the first link, to prevent you from being stuck in an infinent loop.

from bs4 import BeautifulSoup as BS

def local_links(article, prev_articles):    #finds the first valid unvisited article link for a given wikipedia page
    from pattern.web import *
    w = Wikipedia()
    end = [0]
    for i in range(5):  #finds where the first paragraph is, if the paragraph doesn't have a valid link, it moves on to the next <p>
        article_page = w.search(article)
        start = article_page.source.find("<p>",end[-1],len(article_page.source))
        end.append(article_page.source.find("</p>", start,len(article_page.source)))
        if '(' in article_page.source[start:end[-1]] and '_(' not in article_page.source[start:end[-1]]:    #finds parenthesis and excludes them from the paragraph
            parenstart = article_page.source.find("(",start, end[-1])
            parenend = article_page.source.find(")",start, end[-1]) + 1
            article_source = article_page.source[start:parenstart] + article_page.source[parenend:end[-1]]
            paragraph = BS(article_source)
        else:
            paragraph = BS(article_page.source[start:end[-1]])
        links = []
        for link in paragraph.find_all("a"):   #finds all the links in the paragraph using the <a href> tag
            links.append(link['href'])
        for linknumber in range(len(links)):
            if '/wiki/' in links[linknumber]:   #marks things with /wiki/ as valid article links and removes the /wiki/
                startlink = links[linknumber].find('/wiki/') + len('/wiki/')
                endlink = len(links[linknumber])
                links[linknumber] = links[linknumber][startlink:endlink]
                if 'disambiguation' not in links[linknumber] and '#' not in links[linknumber] and 'File:' not in links[linknumber] and 'Wikipedia:' not in links[linknumber] and  'Help:' not in links[linknumber] and '.ogg' not in links[linknumber]:     #filters out a bunch of stuff that aren't article links
                    links[linknumber] =  links[linknumber].replace('_',' ')
                    if links[linknumber] != prev_articles and links[linknumber] not in prev_articles:  #checks if the link has been visited before
                        return links[linknumber]

def philosophy_game(origin):    #runs the local_links loop to click on the first link on every new article page until it reaches the philosophy page
    journey = [origin, local_links(origin, origin)]
    print journey[1] + '...'
    while journey[-1] != 'Philosophy':
        journey.append(local_links(journey[-1],journey))    #creates a list of all the visited pages
        print journey[-1].encode('utf-8') + '...'
    print 'OMG Philosophy!'
    print 'Your journey here:'
    return journey

print 'Wikipedia plays philosophy for you:'

origin = raw_input('Pick a random article: ')   #user input for a valid existing wikipedia article
print philosophy_game(origin)