from twilio.rest import Client

# Twilio credentials (replace with your own)
AUTH_TOKEN = ''      # Replace with your Twilio Auth Token
TWILIO_PHONE_NUMBER = ''  # Your Twilio phone number

def make_call(to_phone_number):
    # Create a Twilio client
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    # Define the message to say
    message_body = "Hello! This is a test call from your Twilio application."

    try:
        # Initiate the call
        call = client.calls.create(
            to=to_phone_number,
            from_=TWILIO_PHONE_NUMBER,
            twiml=f'<Response><Say>{message_body}</Say></Response>'  # Voice message via TwiML
        )
        print(f"Call initiated successfully to {to_phone_number}: Call SID {call.sid}")
    except Exception as e:
        print(f"Failed to make the call: {str(e)}")

# Example usage
if __name__ == "__main__":
    recipient_number = input("Enter the recipient's phone number (include country code): ")
    make_call(recipient_number)
