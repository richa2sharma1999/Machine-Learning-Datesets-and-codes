import nltk
import nltk.corpus
import nltk.stem.porter

porter_stemmer=nltk.stem.porter.PorterStemmer()
print(porter_stemmer.stem('going'))#takes a word and convert it into tokens

print(set(nltk.corpus.stopwords.words('english')))#show all the stop-words
