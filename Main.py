import Scraper
import json
from multiprocessing import Pool
from itertools import chain

def keyword_search(query,amount):
    pmc_ids= [pmc for pmc in Scraper.esearch(query, amount)]
    alltext = [i for i in Scraper.text_grab_multiple(pmc_ids)]
    keywords = [i.lower() for i in Scraper.get_continuous_chunks(" ".join(alltext), query)]
    return keywords[:7]

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
    with open('static/networks/network.json','w') as f:
        json.dump(data,f)

def main_scraper(topic):

    data = {}
    data[topic] = keyword_search(topic,'15')
    #scraping concurrency for keyword sub-searches
    with Pool() as p:
        results = p.map(sub_search, data[topic])

    for i,j in enumerate(data[topic]):
        data[j] = results[i]

    # for i in data[topic]:
        # data[i] = [i for i in keyword_search(i,'10')]

        # all_nodes = ' '.join([k+' '+' '.join(v) for k,v in data.items()])
        # for j in data[i]:
        #     if (j in all_nodes) or (j in all_nodes+'s'):
        #         data[i].remove(j)

    json_networker(data)


