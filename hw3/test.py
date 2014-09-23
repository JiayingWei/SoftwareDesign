def local_links(article, prev_articles):

    from pattern.web import *
    w = Wikipedia()
    article = w.search(article)
    while hasattr(article,'links') == False:
        for i in range(len(prev_articles)):
            article = w.search(prev_articles[-i])
            if hasattr(article,'links') == True:
                break
    link = article.links
    for i in range(len(link)):
        if link[i] not in prev_articles:
            return link[i]

def philosophy_game(origin):
    journey = [origin, local_links(origin, origin)]
    while journey[-1] != 'Philosophy':
        # if len(journey) == 1:
        #   journey.append(local_links(journey[-1],journey[-1]))
        # else:
        journey.append(local_links(journey[-1],journey))
        print 'printing journey things:'
        print journey
    return journey

philosophy_game('Reality')
