from flask import Flask, render_template, request, redirect, url_for, flash
from twilio.rest import Client
import os

app = Flask(__name__)

# Secret key for flashing messages (optional, used to display success/failure messages)
app.secret_key = 'your_secret_key'

# Twilio credentials (ensure you store these in environment variables for security)
ACCOUNT_SID = ''  # Replace with your Twilio Account SID
AUTH_TOKEN = ''    # Replace with your Twilio Auth Token
TWILIO_PHONE_NUMBER = ''  # Your Twilio phone number

client = Client(ACCOUNT_SID, AUTH_TOKEN)

@app.route('/')
def home():
    return render_template('send sms.html')

@app.route('/send_sms', methods=['POST'])
def send_sms():
    phone_number = request.form['phone']
    message_body = request.form['message']

    try:
        message = client.messages.create(
            body=message_body,
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        flash(f"SMS sent successfully to {phone_number}: Message SID {message.sid}", 'success')
        return redirect(url_for('home'))
    except Exception as e:
        flash(f"Failed to send SMS: {str(e)}", 'danger')
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
