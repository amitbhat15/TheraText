from rasa_nlu.model import Metadata, Interpreter
import spacy
nlp = spacy.load("en")
docx = nlp("I am looking for an Italian restaurant where I can eat")
for word in docx.ents:
    print("value: ",word.text,"entity: ", word.label_)

interpreter = Interpreter.load("/Users/advaitmarathe/Documents/ML/default/model_20191020-011828")
print(interpreter.parse("I am looking for an Italian restaurant where I can eat"))