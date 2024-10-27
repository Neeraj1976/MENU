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

print("Welcome to our App")

print("""
press 1: Rainbow Colored terminal..... ++
press 2: Create Your Own WebPage fully Automated... ++
press 3: call someone
press 4: Mail someone.....
press 5: scrape top 5 results
press 6: schedule an email
press 7: send email with image attachment
press 8: Live Streaming Through Mobile Cam......   ++
press 9: Live Video Streaming.....
press 10: Print data in tabular Format....  ++
press 11: Search Students by College Name.....  ++
""")

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

ch = input("Enter your choice: ")

if int(ch) == 1:
    colorama.init()
    text = "RAINBOW"
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']

    for i, letter in enumerate(text):
        color = colors[i % len(colors)]
        print(colored(letter, color), end='')
    print()

elif int(ch) == 2:
    user_inputs = []

    print("Enter your inputs one by one. Type 'done' when you are finished:")

    while True:
        user_input = input("Enter input: ")
        if user_input.lower() == 'done':
            break
        user_inputs.append(user_input)

    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>User Input Form</title>
    </head>
    <body>
        <h1>Hands-Free Developed Form for You....</h1>
        <form action="/submit" method="post">
    """

    for input_name in user_inputs:
        html_content += f'        <label for="{input_name}">{input_name.capitalize()}:</label>\n'
        html_content += f'        <input type="text" id="{input_name}" name="{input_name}"><br><br>\n'

    html_content += """
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    """

    with open("form.html", "w") as file:
        file.write(html_content)

    print("HTML form has been created and saved as 'form.html'.")

elif int(ch) == 3:
     html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>User Input Form</title>
    </head>
    <body>
        <h1>Your Own Search Web UI..</h1>
        <form action="/submit" method="post">
    """

    for input_name in user_inputs:
        html_content += f'        <label for="{input_name}">{input_name.capitalize()}:</label>\n'
        html_content += f'        <input type="text" id="{input_name}" name="{input_name}"><br><br>\n'

    html_content += """
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    """

    with open("form.html", "w") as file:
        file.write(html_content)

    print("HTML form has been created and saved as 'form.html'.")

elif int(ch) == 4:
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

    sender_email = "ranjansanjeev07@gmail.com"
    receiver_email = input("Enter receiver Mail ID: ")
    password = "zyce vayi zjdk izww"
    subject = input("Enter subject of Mail: ")
    body = input("Enter body of Mail: ")
    send_email(sender_email, receiver_email, password, subject, body)

elif int(ch) == 5:
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

elif int(ch) == 6:
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

    sender_email = "ranjansanjeev07@gmail.com"
    receiver_email = input("Enter receiver email: ")
    password = "zyce vayi zjdk izww"
    subject = input("Enter subject of email: ")
    body = input("Enter body of email: ")
    send_time = input("Enter time to send email (HH:MM format): ")
    schedule_email(sender_email, receiver_email, password, subject, body, send_time)

elif int(ch) == 7:
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

    def send_email_with_attachment(sender_email, receiver_email, password, subject, body, attachment_path):
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
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

    image_filename = "captured_image.jpg"
    capture_image(image_filename)

    sender_email = "ranjansanjeev07@gmail.com"
    receiver_email = input("Enter Mail ID: ")
    password = "zyce vayi zjdk izww"
    subject = "Subject: Image Attachment"
    body = "This email contains an image attachment."
    send_email_with_attachment(sender_email, receiver_email, password, subject, body, image_filename)

elif int(ch) == 8:
    cap = cv2.VideoCapture("")
    while True:
        status, photo = cap.read()
        photo[0:220,470:640] = photo[130:350, 280:450]
        cv2.imshow("Ankit photo", photo)
        if cv2.waitKey(80) == 13:
            break
    cv2.destroyAllWindows()
    cap.release()

elif int(ch) == 9:
    cap = cv2.VideoCapture(0)
    while True:
        status, photo = cap.read()
        photo[0:220,470:640] = photo[130:350, 280:450]
        cv2.imshow("Ankit photo", photo)
        if cv2.waitKey(80) == 13:
            break
    cv2.destroyAllWindows()
    cap.release()

elif int(ch) == 10:
    headers = ["Name", "City", "College", "Whatsapp Number", "Life Purpose"]
    table = []
    for person in team_data:
        table.append([person[header] for header in headers])
    print(tabulate(table, headers=headers, tablefmt="grid"))
    print("Thanks for using our Integrated System........")

elif int(ch) == 11:
    def search_by_college(college_name):
        results = [person["Name"] for person in team_data if person["College"] == college_name]
        return results

    college_name = input("Enter college name : ")
    students = search_by_college(college_name)

    print(f"Students from {college_name}: {', '.join(students)}")
    print("Thanks for using our Integrated System........")

else:
    print("Invalid choice, please try again.")

