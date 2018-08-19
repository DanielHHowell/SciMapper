import requests
from xml.etree.ElementTree import fromstring


def esearch(topic_input, nResults):
    # Formats the terms for the API search
    topic = '%22' + topic_input.replace(' ', '+') + '%22'
    base_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pmc&api_key=c3b9ad9a1cb4e93717881a2421f597b1ae08&sort=' + '&retmax=' + nResults + '&term='
    r = requests.get(base_url + topic)
    xmltree = fromstring(r.content)
    PMCIDs = [i.text for i in xmltree[3]]

    return PMCIDs, topic_input