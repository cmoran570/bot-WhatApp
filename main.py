import openai
import config
from flask import Flask, request
from twilio.rest import Client

openai.api_key = config.api_key
account_sid = config.account_sid
auth_token = config.auth_token



app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])

def chatbot_response(message):
    response = openai.completions.create(model='gpt-3.5-turbo-instruct',
                                      prompt=input,
                                      max_tokens=2048
                                      )

    completion = response.choices[0].text
    return completion

   
def handle_incoming_message():
    mesagge = request.form['Body']
    # Generate response with chatbot
    response = chatbot_response(mesagge)
    
    # Send response to whatsapp
    client = Client(account_sid, auth_token)
    number = request.form['From']
    
    to_number = number
    client.messages.create(
        to=to_number,
        from_='whatsapp:+14155238886',
        body=response
        )

    # Send response to twilio
    return 'Return: OK'

if __name__ == '__main__':
    app.run()