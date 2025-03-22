from dotenv import load_dotenv
import smtplib, os
from email.mime.text import MIMEText
from datetime import date
load_dotenv()
 
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')  
SENDER_EMAIL = os.getenv('SENDER_EMAIL')  
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')  

def send_email(bot_message, asset_name):
    current_date = date.today()
    """Send an email alert."""
    subject = f"INVESTMENT REPORT: {asset_name}, DATE: {current_date}\n"
    body = f"{bot_message}"
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, EMAIL_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
            print("Email alert sent!")
            
    except Exception as e:
        print(f"Error sending email: {e}")
        