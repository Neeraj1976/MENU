
from flask import Flask

app = Flask(__name__)

from twilio.rest import Client
import pywhatkit
import smtplib
import schedule
import time
from email.mime.text import MIMEText
import requests
from bs4 import BeautifulSoup
from googlesearch import search
import cv2
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from tabulate import tabulate
from termcolor import colored
import colorama

team_data = [
    {"Name": "Aarav", "City": "Mumbai", "College": "Indian Institute of Technology Bombay", "Whatsapp Number": "1234567890", "Life Purpose": "Empowerment"},
    {"Name": "Bhairavi", "City": "Delhi", "College": "Delhi University", "Whatsapp Number": "9876543210", "Life Purpose": "Innovation"},
    {"Name": "Chirag", "City": "Bangalore", "College": "Indian Institute of Science", "Whatsapp Number": "5678901234", "Life Purpose": "Creativity"},
    {"Name": "Divya", "City": "Hyderabad", "College": "Osmania University", "Whatsapp Number": "4567890123", "Life Purpose": "Impact"},
    {"Name": "Eshaan", "City": "Chennai", "College": "Anna University", "Whatsapp Number": "2345678901", "Life Purpose": "Discovery"},
    {"Name": "Falguni", "City": "Kolkata", "College": "Jadavpur University", "Whatsapp Number": "7890123456", "Life Purpose": "Invention"},
    {"Name": "Gautam", "City": "Pune", "College": "Savitribai Phule Pune University", "Whatsapp Number": "8901234567", "Life Purpose": "Philanthropy"},
    {"Name": "Harsh", "City": "Ahmedabad", "College": "Indian Institute of Management Ahmedabad", "Whatsapp Number": "3456789012", "Life Purpose": "Exploration"},
    {"Name": "Isha", "City": "Jaipur", "College": "Malaviya National Institute of Technology Jaipur", "Whatsapp Number": "9012345678", "Life Purpose": "Education"},
    {"Name": "Jatin", "City": "Lucknow", "College": "University of Lucknow", "Whatsapp Number": "6789012345", "Life Purpose": "Adventure"},
    {"Name": "Kriti", "City": "Bhopal", "College": "Maulana Azad National Institute of Technology Bhopal", "Whatsapp Number": "2345678901", "Life Purpose": "Leadership"},
    {"Name": "Lakshya", "City": "Patna", "College": "Indian Institute of Technology Patna", "Whatsapp Number": "4567890123", "Life Purpose": "Innovation"},
    {"Name": "Meera", "City": "Kanpur", "College": "Indian Institute of Technology Kanpur", "Whatsapp Number": "5678901234", "Life Purpose": "Creativity"},
    {"Name": "Nikhil", "City": "Indore", "College": "Indian Institute of Technology Indore", "Whatsapp Number": "6789012345", "Life Purpose": "Discovery"},
    {"Name": "Ojas", "City": "Thiruvananthapuram", "College": "Indian Institute of Space Science and Technology", "Whatsapp Number": "7890123456", "Life Purpose": "Impact"},
    {"Name": "Prisha", "City": "Ranchi", "College": "Indian Institute of Management Ranchi", "Whatsapp Number": "8901234567", "Life Purpose": "Empowerment"},
    {"Name": "Qasim", "City": "Surat", "College": "Sardar Vallabhbhai National Institute of Technology Surat", "Whatsapp Number": "9012345678", "Life Purpose": "Innovation"},
    {"Name": "Rhea", "City": "Vadodara", "College": "Maharaja Sayajirao University of Baroda", "Whatsapp Number": "1234567890", "Life Purpose": "Creativity"},
    {"Name": "Samar", "City": "Guwahati", "College": "Indian Institute of Technology Guwahati", "Whatsapp Number": "2345678901", "Life Purpose": "Impact"},
    {"Name": "Tanvi", "City": "Visakhapatnam", "College": "Andhra University", "Whatsapp Number": "3456789012", "Life Purpose": "Discovery"}
]



def whatmsg():
	user_num = input("Enter the number to whom you want to send a message (in format +<country code><number>): ")
	msg = input("Enter your message here: ")
	time_hr = int(input("Enter time in hour (24-hour format): "))
	time_min = int(input("Enter time in minute: "))
	pywhatkit.sendwhatmsg(user_num, msg, time_hr, time_min)
	print("Message sent successfully.....")









#send sms
def Sendsms():
	account_sid = '' #add your twilio account SID
	auth_token = '' #add your twilio account Token
	client = Client(account_sid, auth_token)

	twilio_phone_number = '' #add your twilio number
	recipient_phone_number = input("Enter recipient number (linked with Twilio): ")

	message = client.messages.create(
        body=input("Enter your text message: "),
	from_=twilio_phone_number,
	to=recipient_phone_number
	)
	print(f"Message sent successfully. SID: {message.sid}")


#call someone
def PhoneCall():
    account_sid = '' #add your twilio account SID
    auth_token = ''#add your twilio account Token
    client = Client(account_sid, auth_token)

    twilio_phone_number = '' #add your twilio number
    recipient_num = input("Enter number to call (in format +<country code><number>): ")

    twiml_url = 'http://demo.twilio.com/docs/voice.xml'

    call = client.calls.create(
        to=recipient_num,
        from_=twilio_phone_number,
        url=twiml_url
    )

    print(f"Call is going on.....Call SID: {call.sid}")


#send mail
def sendEmail():
    def send_email(sender_email, receiver_email, password, subject, body):
        message = MIMEText(body)
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully.")
        except Exception as e:
            print(f"Error sending email: {e}")

    sender_email = ""
    receiver_email = input("Enter receiver Mail ID: ")
    password = ""
    subject = input("Enter subject of Mail: ")
    body = input("Enter body of Mail: ")

    send_email(sender_email, receiver_email, password, subject, body)


#scrape top 5 results
def topsearch():
    def scrape_top_5_results(query):
        search_results = search(query, num_results=5)
        results_data = []

        for url in search_results:
            try:
                response = requests.get(url)
                response.raise_for_status()
                soup = BeautifulSoup(response.content, 'html.parser')
                title = soup.title.string if soup.title else 'No title'
                meta_desc = soup.find('meta', attrs={'name': 'description'})
                description = meta_desc['content'] if meta_desc else 'No description'

                results_data.append({
                    'url': url,
                    'title': title,
                    'description': description
                })
            except Exception as e:
                print(f"Failed to scrape {url}: {e}")

        return results_data

    query = input("Enter your query: ")
    results = scrape_top_5_results(query)

    for idx, result in enumerate(results, start=1):
        print(f"Result {idx}:")
        print(f"URL: {result['url']}")
        print(f"Title: {result['title']}")
        print(f"Description: {result['description']}")
        print("-" * 80)


#schedule an email
def scheduleEmail():
    def send_email(sender_email, receiver_email, password, subject, body):
        message = MIMEText(body)
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully.")
        except Exception as e:
            print(f"Error sending email: {e}")

    def schedule_email(sender_email, receiver_email, password, subject, body, send_time):
        schedule.every().day.at(send_time).do(send_email, sender_email, receiver_email, password, subject, body)
        while True:
            schedule.run_pending()
            time.sleep(1)

    sender_email = ""
    receiver_email = input("Enter receiver email: ")
    password = ""
    subject = input("Enter subject of email: ")
    body = input("Enter body of email: ")
    send_time = input("Enter time to send email (HH:MM format): ")

    schedule_email(sender_email, receiver_email, password, subject, body, send_time)


#send email with image attachment
def email_attachment():
    # Function to capture an image using OpenCV
    def capture_image(filename):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Could not open webcam")
            return
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(filename, frame)
            print(f"Image saved as {filename}")
        cap.release()
        cv2.destroyAllWindows()

    # Function to send an email with an attachment
    def send_email_with_attachment(sender_email, receiver_email, password, subject, body, attachment_path):
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        
        message.attach(MIMEText(body, 'plain'))

        # Attach the file
        with open(attachment_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={attachment_path}')
            message.attach(part)

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully.")
        except Exception as e:
            print(f"Error sending email: {e}")

    # Capture the image
    image_filename = "captured_image.jpg"
    capture_image(image_filename)

    # Send the email
    sender_email = ""
    receiver_email = input("Enter Mail ID: ")
    password = ""
    subject = "Subject: Image Attachment"
    body = "This email contains an image attachment."

    send_email_with_attachment(sender_email, receiver_email, password, subject, body, image_filename)


#to run a train    
def runTrain():
    os.system("sl")


#Live Video Streaming
def liveStream():
    cap = cv2.VideoCapture(0)

    while True:
        status, photo = cap.read()
        photo[0:220,470:640] = photo[130:350, 280:450]
        cv2.imshow("Rahul photo", photo)
        if cv2.waitKey(80) == 13:
            break

    cv2.destroyAllWindows()
    cap.release()

#Print data in tabular Format
def studentdata():
    table_headers = ["Name", "City", "College", "Whatsapp Number", "Life Purpose"]
    table_rows = [
        [member["Name"], member["City"], member["College"], member["Whatsapp Number"], member["Life Purpose"]]
        for member in team_data
    ]
    print(tabulate(table_rows, headers=table_headers, tablefmt="grid"))


#Rainbow color
def rainbowColor():
	# Initialize colorama for Windows support

	colorama.init()

	# Define the text and the colors

	text = "RAINBOW"

	colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']



	# Print each letter in a different color

	for i, letter in enumerate(text):

	    color = colors[i % len(colors)]

	    print(colored(letter, color), end='')



	# Print a newline at the end

	print()


#live video through mobile cam	
def mobile_cam():

	cap = cv2.VideoCapture("https://192.168.51.102:8080/video")

	while True:
	    status, photo = cap.read()

	    cv2.imshow("Rahul photo", photo)
	    if cv2.waitKey(80) == 13:  # Break the loop if 'Enter' key is pressed
             break

	cv2.destroyAllWindows()
	cap.release()


#Search Students by College Name.....
def searchStudent():
    def search_students_by_college(college_name):
        return [member for member in team_data if college_name.lower() in member["College"].lower()]

    college_name = input("Enter college name to search for students: ")
    matching_students = search_students_by_college(college_name)
    if matching_students:
        print("Matching students:")
        for student in matching_students:
            print(f"Name: {student['Name']}, City: {student['City']}, College: {student['College']}, Whatsapp Number: {student['Whatsapp Number']}, Life Purpose: {student['Life Purpose']}")
    else:
        print("No students found for the given college name.")


#Create Your Own WebPage fully Automated...
def webpage():
    html_content = """
    <html>
    <head>
        <title>My Automated Webpage</title>
    </head>
    <body>
        <h1>Welcome to My Automated Webpage</h1>
        <p>This webpage is created using a Python script.</p>
        <p>Feel free to customize this template as per your needs.</p>
    </body>
    </html>
    """
    with open("automated_webpage.html", "w") as file:
        file.write(html_content)
    print("Webpage created successfully. Check the file 'automated_webpage.html'.")


