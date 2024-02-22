import smtplib
import ssl
from email.message import EmailMessage
from bs4 import BeautifulSoup
import pandas as pd

# Login credentials
SENDER = "youremail@example.com"
PASSWORD = "app password key"

# Get list of receivers and names
forms = 'docs\\info.xlsx'
df = pd.read_excel(forms)
receivers = dict(zip(df['Email'], df['Name']))

# Get the HTML email as well as the Subject
with open('html\\index.html', 'r') as file:
    base_body = file.read()

soup = BeautifulSoup(base_body, 'html.parser')
titles = soup.find_all('title')
subject = titles[0].text if titles else 'Update!'

# Secure connection context
context = ssl.create_default_context()

print("Sending Emails!")

for receiver, name in receivers.items():
    # Personalize your emails!
    personalized_body = base_body.replace('[[name]]', name)
    
    # Initialize Email Message
    message = EmailMessage()
    message["From"] = SENDER
    message["To"] = receiver
    message["Subject"] = subject
    message.add_alternative(personalized_body, subtype="html")
    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(SENDER, PASSWORD)
            server.sendmail(SENDER, receiver, message.as_string())
        print(f"Email successfully sent to: {receiver}")
    except Exception as e:
        print(f"Error sending email to: {receiver}, {e}")

print("Successfully sent emails. Check your inboxes.")
