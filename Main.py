from multiprocessing import Pool
import PageScraper
import KeywordAnalysis
import json
from itertools import chain

def keyword_search(query,amount):
    pmc_ids= [pmc for pmc in PageScraper.esearch(query, amount)]
    alltext = [KeywordAnalysis.text_grab(i) for i in pmc_ids]
    keywords = [i.lower() for i in KeywordAnalysis.get_continuous_chunks(" ".join(alltext), query)]
    return keywords[:10]

def sub_search(keyword):
    kwds = [i for i in keyword_search(keyword, '15')]
    return kwds

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
    with open('/home/daniel/PycharmProjects/scimapper/static/networks/network.json','w') as f:
    #with open('static/networks/network.json','w') as f:
        json.dump(data,f)

def main_scraper(topic):

    data = {}
    data[topic] = keyword_search(topic,'20')

    #scraping concurrency for keyword sub-searches
    with Pool() as p:
        results = p.map(sub_search, data[topic])
    
    for i,j in enumerate(data[topic]):
        data[j] = results[i]
    
    #for i in data[topic]:
    #    data[i]=keyword_search(i, '9')
	#data[i] = [i for i in keyword_search(i,'10')]
        # for j in data[i]:
        #     if (j in all_nodes) or (j in all_nodes+'s'):
        #         data[i].remove(j)
    json_networker(data)

#main_scraper('ibuprofen')

