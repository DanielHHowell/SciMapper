from nltk import *
import requests
from collections import Counter

def text_grab(pmc):
    abstract_url = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id='
    search_abstract = abstract_url + pmc + '&retmode=report_type&rettype=medline&api_key=c3b9ad9a1cb4e93717881a2421f597b1ae08'
    r2 = requests.get(search_abstract).text
    abstract = r2[r2.find('AB') + 6:r2.find('FAU')]
    return abstract


def get_continuous_chunks(article_text):
    stopwords = ['et', 'al.', 'n', 'deviation', 'windowFigure', 'windowFig', ' ]',
                 'additional', 'data', 'file', ' ', 'distribution', 'significant',
                 'clinical', 'adverse', 'sample', 'studies', 'significance',
                 '<', '>', '=', 'window', 't', 't-test', 'supplementary',
                 'important','experimental', 'study', 'subjects', 'conditions', 'experiments',
                 'control', 'panel', 'outcomes', 'response', 'standardized', '[']
    words = word_tokenize(article_text)
    filtered_text = [w.lower() for w in words if w.lower() not in stopwords]
    processed_text = pos_tag(filtered_text)

    # Regex to grammatically identify a set of: adjective+noun(+noun)
    # From NLTK: JJ* = adjective/numeral/ordinal/comparative/superlative, NN* = Nouns
    chunk_gram = r"Chunk: {<JJ.?><NN.?>?<NN.?>}"
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

    counted = Counter(newkeys).most_common(6)
    keywords = [i[0] for i in counted]
    return keywords
