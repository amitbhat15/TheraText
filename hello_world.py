# hello_world.py

# from flask import Flask
# from flask import render_template
# app = Flask(__name__)


# @app.route('/sms')
# def hello_world():
#     return 'Hello World!'

# @app.route('/sms')
# def hello_world():
#     return render_template("somefile.html")

# from flask import Flask, request, redirect
# from twilio.twiml.messaging_response import MessagingResponse

# app = Flask(__name__)

# @app.route("/sms", methods=['GET', 'POST'])
# def sms_reply():
#     """Respond to incoming calls with a simple text message."""
#     # Start our TwiML response
#     resp = MessagingResponse()

#     # Add a message
#     resp.message("The Robots are coming! Head for the hills!")

#     return str(resp)

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from rasa_nlu.model import Metadata, Interpreter
import spacy
import json
nlp = spacy.load("en")
interpreter = Interpreter.load("/Users/samarth/my-project/TheraText-master/default/model_20191020-134022")

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)
    # Start our TwiML response
    resp = MessagingResponse()
    message = interpreter.parse(body);
    intent = message['intent']
    ans = str(str(intent['name']) + ' ' + str(intent['confidence']))
    resp.message(str(ans))
    
    return str(resp)
    # return str(resp)

if __name__ == "__main__":
    app.run(debug=True)