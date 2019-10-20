from rasa_nlu.model import Metadata, Interpreter
import spacy
import json
nlp = spacy.load("en")
interpreter = Interpreter.load("default/model_20191020-123549")
message = interpreter.parse("Hey")
intent = message['intent']
email_message = "negative mood"
if(intent['name'] == 'negative' and intent['confidence'] > 0.6):
    email_message = "negative mood"
else:
    email_message = "positive mood"

final_message = "Your patient has been experiencing a " + email_message +". You should schedule an appointment to check up on them."
print(final_message)
message = interpreter.parse("Something happened today")
messages = ['Hey',"Something happened today", "I could not get any work done","I feel depressed", "I felt happy today", "I felt tired"]
for i in messages:
    message = interpreter.parse(i);
    intent = message['intent']
    print(intent['name'], intent['confidence'])


