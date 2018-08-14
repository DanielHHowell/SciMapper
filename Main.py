import PageScraper
import KeywordAnalysis
import json

#def keywword_search(search):

mainpmc_ids, mainquery = [pmc for pmc in PageScraper.esearch('LSD', None, '10', 'relevance')]
mainalltext = [KeywordAnalysis.text_grab(i) for i in mainpmc_ids]
mainkeywords = [i.lower() for i in KeywordAnalysis.get_continuous_chunks(" ".join(mainalltext)) if i != 'grid cells']
maindatadict = {}
maindatadict[mainquery] = mainkeywords
for i in mainkeywords:
    pmc_ids, query = [pmc for pmc in PageScraper.esearch(i, None, '10', 'relevance')]
    alltext = [KeywordAnalysis.text_grab(j) for j in pmc_ids]
    keywords = [k.lower() for k in KeywordAnalysis.get_continuous_chunks(" ".join(alltext)) if k != i]
    maindatadict[query] = keywords
print(maindatadict)


def json_networker(dict):
    nodes, links = (set() for i in range(2))
    for k,v in dict.items():
        nodes.add(k)
        for i in v:
            nodes.add(i)
            links.add((k,i))
    data = {}
    data['nodes'] = [{"id":node} for node in nodes]
    data['links'] = [{"source":link[0],"target":link[1],"value":10} for link in links]
    with open('network.json','w') as f:
        json.dump(data,f)

json_networker(maindatadict)