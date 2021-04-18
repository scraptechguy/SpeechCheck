from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import pandas as pd


text = "Hey, how are you? I'm doing well so far. Thanks for asking. How are you? Nothing fancy, just great. I'm being distracted by you now. I was not aware of that, sorry."

# breaking down a text paragraph to sentenses

tokenized_sent=sent_tokenize(text)
print(tokenized_sent)


# breaking down a text paragraph to words

tokenized_word=word_tokenize(text)
print(tokenized_word)


# displaying number of samples and outcomes

fdist = FreqDist(tokenized_word)
print(fdist)


# finding most common word (or words, for that change number in brackets)

print(fdist.most_common(1))


# filtering stopwords 

stop_words=set(stopwords.words("english"))

filtered_sent=[]
for w in tokenized_sent:
    if w not in stop_words:
        filtered_sent.append(w)
print("Tokenized Sentence:",tokenized_sent)
print("Filterd Sentence:",filtered_sent)
