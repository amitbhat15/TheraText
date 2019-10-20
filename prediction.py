from rasa_nlu.model import Metadata, Interpreter
import spacy
import json
nlp = spacy.load("en")
docx = nlp("I am looking for an Italian restaurant where I can eat")
for word in docx.ents:
    print("value: ",word.text,"entity: ", word.label_)

interpreter = Interpreter.load("/Users/advaitmarathe/Documents/ML/default/model_20191020-045928")
message = interpreter.parse(" ")
print(message)
intent = message['intent']
print(intent)
email_message = "negative mood"
if(intent['name'] == 'negative'):
    email_message = "negative mood"
else:
    email_message = "positive mood"

final_message = "Your patient has been experiencing a " + email_message + ". You should schedule an appointment to check up on them."

