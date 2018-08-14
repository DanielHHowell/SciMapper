import requests
from lxml import html
from xml.etree.ElementTree import fromstring


def esearch(topic_input, queries, nResults, sortby):
    # Formats the terms for the API search
    topic = '%22' + topic_input.replace(' ', '+') + '%22'
    if queries:
        query_terms = [i.strip() for i in queries.split(',')]
        boolean_queries = '+OR+'.join(query_terms)
        search_terms = topic + '+AND+%28' + boolean_queries + '%29'
    else:
        search_terms = topic

    base_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pmc&api_key=c3b9ad9a1cb4e93717881a2421f597b1ae08&sort=' + sortby + '&retmax=' + nResults + '&term='
    r = requests.get(base_url + search_terms)
    xmltree = fromstring(r.content)
    PMCIDs = [i.text for i in xmltree[3]]

    # Formats the search  for use in the report title, returning 'query'
    printable_search = topic_input
    if queries:
        printable_search += ':'
        for i in query_terms:
            printable_search += ' ' + i + ','
        printable_search = printable_search[:-1]
    query = printable_search

    return PMCIDs, query