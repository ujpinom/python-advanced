from textblob import TextBlob

text='Today is a beautiful day. Tomorrow looks like bad weather.'
blob= TextBlob(text);print(blob)
#TextBlob soporta metodos para oraciones y palabras en textos

#Tokenizing text into sentences and words; Let's use setence property to get a list o sentence objects
print(blob.sentences,blob.words);# blob.senteces retorna una lista con la oraciones que hay en el texto.blob.words retorna las palabras que hay en el texto. Todos los retornos son en forma de lista
print(blob.words[0])

#---------------------Parts-of-Speech Tagging------------------------------------------------------------

#There are eight primary English parts of speech— nouns, pronouns, verbs, adjectives, adverbs, prepositions, conjunctions and interjections
# (words that express emotion and that are typically followed by punctuation, like “Yes!” or “Ha!”).

print(blob.tags)

##------------------------- extracting noun phrases.------------------------
print(blob.noun_phrases)
############-------------------Sentiment Analysis with TextBlob’s Default Sentiment Analyzer------------------
#For instance, companies might use this to determine whether people are speaking positively or negatively online about their products.
############333333333333 ----------------------        Getting the Sentiment of a TextBlob
print(blob.sentiment)
#---------------------------------------- Sentiment Analysis with the NaiveBayesAnalyzer------------------------
from textblob.sentiments import NaiveBayesAnalyzer
blob= TextBlob(text,analyzer=NaiveBayesAnalyzer()); print(blob.sentiment)
print(blob.translate(to='es'))