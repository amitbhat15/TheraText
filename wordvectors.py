from __future__ import unicode_literals
import spacy
from spacy import displacy
import math
import pandas as pd
from spacy.lang.en.stop_words import STOP_WORDS

nlp = spacy.load('en')
docx = nlp(u"Spacy is a cool tool")
docx2 = nlp(u"Spacy is an amazing tool like nltk")

myFile = open("input.txt").read()
docFile= nlp(myFile)
#print(docFile)
for num, sentence in enumerate(docFile.sents):
    print(num,sentence)
ex1 = nlp("Sri is a dog")
for word in ex1:
    print(word.text,word.tag_,spacy.explain(word.tag_))

# excercise2 = nlp("This is going to be super cool")
# ex3 = nlp("Whats the dependency of all of these words on each other and how much can I fuck up the system")
# displacy.serve(ex3, style = "dep")

docx = nlp("study studying studious studio student")
for word in docx:
    print(word.text,word.lemma_,word.pos_)
wikitext = nlp("Sad Depression Sadness kill myself")
for word in wikitext.ents:
    print(word.text,word.label_)
#displacy.serve(wikitext,style ='ent')
ex1 = nlp("wolf dog cat bird fish")
for word1 in ex1:
    for word2 in ex1:
        print((word1.text,word2.text), "Similarity", word1.similarity(word2))
myList = [(word1.text,word2.text,word1.similarity(word2)) for token2 in ex1 for token1 in ex1]
df = pd.DataFrame(myList)

ex7 = nlp("I do not feel very good")
for t in ex7:
    print(t.is_stop,t)
print([word for word in ex7 if word.is_stop == False])