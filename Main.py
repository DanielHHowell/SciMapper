import PageScraper
import KeywordAnalysis
import json
from itertools import chain

def keyword_search(query,amount):
    pmc_ids= [pmc for pmc in PageScraper.esearch(query, amount)]
    alltext = [KeywordAnalysis.text_grab(i) for i in pmc_ids]
    keywords = [i.lower() for i in KeywordAnalysis.get_continuous_chunks(" ".join(alltext), query)]
    return keywords[:7]

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
    data[topic] = keyword_search(topic,'12')
    for i in data[topic]:
        #all_nodes = ' '.join([k+' '+' '.join(v) for k,v in data.items()])
        data[i] = [i for i in keyword_search(i,'7')]
        # for j in data[i]:
        #     if (j in all_nodes) or (j in all_nodes+'s'):
        #         data[i].remove(j)
    json_networker(data)


