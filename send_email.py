import os
import smtplib
from email.message import EmailMessage

# Load environment variables
EMAIL_ADDRESS = os.getenv('EMAIL_USER')  # More reliable than os.environ.get
EMAIL_PASSWORD = os.getenv('EMAIL_PASS')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')

def send_email():
    try:
        msg = EmailMessage()
        msg['Subject'] = 'Test Email'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL
        msg.set_content('This is a test email')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
        raise  # Re-raise for GitHub Actions to catch 

if __name__ == "__main__":
    send_email()