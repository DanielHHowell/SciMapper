import requests
from xml.etree.ElementTree import fromstring


def esearch(topic_input, nResults):
    # Formats the terms for the API search
    topic = '%22' + topic_input.replace(' ', '+') + '%22'
    base_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pmc&api_key=9893ad891eedcd3802a273ea252798721e08&sort=relevance&retmax=' + nResults + '&term='
    r = requests.get(base_url + topic)
    xmltree = fromstring(r.content)
    PMCIDs = [i.text for i in xmltree[3]]

    return PMCIDs
