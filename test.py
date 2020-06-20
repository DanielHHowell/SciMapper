from nltk import *
import requests
from collections import Counter
import itertools
import re
from xml.etree.ElementTree import fromstring

ncbi_api = '9893ad891eedcd3802a273ea252798721e08'

def text_grab_multiple(pmcs):
    pmcs_string = ','.join(pmcs)
    abstract_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id='
    search_abstract = abstract_url + pmcs_string + '&retmode=report_type&rettype=medline&api_key='+ncbi_api
    r = requests.get(search_abstract).text
    records = [i for i in r.split('PMC - PMC')]
    abstracts = [i[i.find('AB') + 6:i.find('FAU')] for i in records]
    for i in abstracts[1:]:
        print(i)

print(text_grab_multiple(['2805706', '5112249']))