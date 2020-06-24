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

def record_grab_multiple(pmcs):
    # Retrieves the Date, Authors, Title and DOI from the API's XML report

    pmcs_string = ','.join(pmcs)
    base_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pmc&id='
    search = base_url + pmcs_string+ '&retmode=report_type&rettype=xml&api_key='+ncbi_api
    r = requests.get(search, stream=True)
    tree = fromstring(r.content)
    pmc_data = dict.fromkeys(pmcs)
    for i,j in enumerate(list(pmc_data)):
        root = tree[i]
        pmc_data[j] = {'Date': root[1].text, 'Authors': [author.text for author in root[4]],
                'Title': root[5].text.title(), 'DOI': root[10].text}
    #
    #
    print(pmc_data)

record_grab_multiple(['2805706', '2805708'])