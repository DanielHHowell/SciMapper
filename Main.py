import PageScraper
import KeywordAnalysis
import json

def keyword_search(search,amount):
    pmc_ids, query = [pmc for pmc in PageScraper.esearch(search, amount)]
    alltext = [KeywordAnalysis.text_grab(i) for i in pmc_ids]
    keywords = [i.lower() for i in KeywordAnalysis.get_continuous_chunks(" ".join(alltext)) if i != search]
    return keywords

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
    with open('/home/DanielHHowell/scimapper/static/networks/network.json','w') as f:
        json.dump(data,f)

def main_scraper(topic):
    data = {}
    data[topic] = keyword_search(topic,'5')
    for i in data[topic]:
        data[i] = keyword_search(i,'5')
    json_networker(data)


#main_scraper('ibuprofen')