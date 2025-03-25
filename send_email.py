import os
import smtplib
from email.message import EmailMessage

# Load credentials from environment variables
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
RECIPIENT_EMAIL = os.environ.get('RECIPIENT_EMAIL')

def send_email():
    msg = EmailMessage()
    msg['Subject'] = 'Automated Email from GitHub Actions'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg.set_content('This email was sent automatically every 20 minutes!')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print("Email sent successfully!")

if __name__ == "__main__":
    send_email()