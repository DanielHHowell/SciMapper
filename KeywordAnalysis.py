from nltk import *
import requests
from collections import Counter
import itertools
import re

def text_grab(pmc):
    abstract_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id='
    search_abstract = abstract_url + pmc + '&retmode=report_type&rettype=medline&api_key=c3b9ad9a1cb4e93717881a2421f597b1ae08'
    r2 = requests.get(search_abstract).text
    abstract = r2[r2.find('AB') + 6:r2.find('FAU')]
    return abstract


def get_continuous_chunks(article_text, query):
    stopwords_s = ['et', 'al.', 'deviation', 'windowFigure', 'windowFig', 'difference',
                 'additional', 'data', 'file', 'distribution', 'significant',
                 'clinical', 'kg', 'adverse', 'sample', 'studies', 'significance',
                 'window', 't-test', 'supplementary', 'important','experimental',
                 'study', 'subject', 'condition', 'experiment', 'control', 'panel',
                 'outcome', 'response', 'standardized', 'publisher', 'abstract',
                 'model', 'event', 'aversive', 'stimulus', 'training', 'risk',
                 'impact', 'article', 'patient', 'adult', 'themes', 'concentration',
                   'participant', 'dose', 'vs', 'normalized', 'mean', 'finding',
                   'incidental',query.lower()]
    stopwords_p = [i+'s' for i in stopwords_s]
    stopwords = stopwords_s+stopwords_p
    token_words = word_tokenize(article_text)
    words = [w.strip() for w in token_words]
    filtered_text = [w for w in words if (w.lower() not in stopwords) and (len(w)>1)]
    processed_text = pos_tag(filtered_text)

    # Regex to grammatically identify a set of: adjective+noun(+noun)
    # From NLTK: JJ* = adjective/numeral/ordinal/comparative/superlative, NN* = Nouns
    chunk_gram = r"Chunk: {<JJ.?><NN.?>}"
    chunk_parser = RegexpParser(chunk_gram)
    chunked = chunk_parser.parse(processed_text)
    keywords = [i.leaves() for i in chunked if type(i) == Tree]
    # NLTK returns chunks in the form of lists of tuples of the word and its pos tag
    newkeys = []
    for chunk in keywords:
        if len(chunk) < 2:
            newkeys.append(list[0][0])
        else:
            temp = []
            for pair in chunk:
                temp.append(pair[0])
            newkeys.append(" ".join(temp))
    counted = Counter(newkeys).most_common(12)

    keywords = [i[0] for i in counted if (i[0]+'s' != query)
                and (i[0] != query+'s')]

    for a,b in itertools.combinations(keywords,2):
        if (a in b.lower()) or (b in a.lower()):
            keywords.remove(b)

    return keywords