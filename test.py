from rake_nltk import Rake
import wikipedia
import KeywordAnalysis

text = wikipedia.page("Neuroscience").content

manual = KeywordAnalysis.get_continuous_chunks(text, 'neuroscience')
print(manual)

r = Rake(min_length=2, max_length=3)
r.extract_keywords_from_text(text)
print(r.get_ranked_phrases())
