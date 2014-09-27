from bs4 import BeautifulSoup as BS

def local_links(article, prev_articles):

    from pattern.web import *
    w = Wikipedia()
    end = [0]
    for i in range(5):
        article_page = w.search(article)
        start = article_page.source.find("<p>",end[-1],len(article_page.source))  #dammit this <ptag>
        end.append(article_page.source.find("</p>", start,len(article_page.source)))
        if '(' in article_page.source[start:end[-1]] and '_(' not in article_page.source[start:end[-1]]:
            parenstart = article_page.source.find("(",start, end[-1])
            parenend = article_page.source.find(")",start, end[-1]) + 1
            article_source = article_page.source[start:parenstart] + article_page.source[parenend:end[-1]]
            paragraph = BS(article_source)
        else:
            paragraph = BS(article_page.source[start:end[-1]])
        links = []
        for link in paragraph.find_all("a"):
            links.append(link['href'])
        for linknumber in range(len(links)):
            if '/wiki/' in links[linknumber]:
                startlink = links[linknumber].find('/wiki/') + len('/wiki/')
                endlink = len(links[linknumber])
                links[linknumber] = links[linknumber][startlink:endlink]
                if 'disambiguation' not in links[linknumber] and '#' not in links[linknumber] and 'File:' not in links[linknumber] and 'Wikipedia:' not in links[linknumber] and  'Help:' not in links[linknumber] and '.ogg' not in links[linknumber]:
                    links[linknumber] =  links[linknumber].replace('_',' ')
                    if links[linknumber] != prev_articles:
                        return links[linknumber]

def philosophy_game(origin):
    journey = [origin, local_links(origin, origin)]
    print journey[1] + '...'
    while journey[-1] != 'Philosophy':
        journey.append(local_links(journey[-1],journey))
        print journey[-1].encode('utf-8') + '...'
    print 'OMG Philosophy!'
    print 'Your journey here:'
    return journey

print 'Wikipedia plays philosophy for you:'

origin = raw_input('Pick a random article: ')
print philosophy_game(origin)
#local_links('Set (Mathematics)','Set (Mathematics)')