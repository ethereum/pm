import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(recipient_email, subject, body):
    """
    Send an email to the recipient with the given subject and body.
    
    Args:
        recipient_email: Email address of the recipient
        subject: Email subject line
        body: HTML body content of the email
    
    Returns:
        bool: True if email was sent successfully, False otherwise
    """
    sender_email = os.environ.get("SENDER_EMAIL")
    sender_password = os.environ.get("SENDER_EMAIL_PASSWORD")
    smtp_server = os.environ.get("SMTP_SERVER")
    smtp_port = os.environ.get("SMTP_PORT", 587)

    if not all([sender_email, sender_password, smtp_server]):
        print(f"[ERROR] Email server credentials are not fully configured.")
        print(f"SENDER_EMAIL: {'Set' if sender_email else 'Missing'}")
        print(f"SENDER_EMAIL_PASSWORD: {'Set' if sender_password else 'Missing'}")
        print(f"SMTP_SERVER: {'Set' if smtp_server else 'Missing'}")
        print(f"SMTP_PORT: {smtp_port}")
        raise Exception("Email server credentials are not fully configured.")

    # Clean up body text by removing leading spaces
    cleaned_body = "\n".join([line.strip() for line in body.split('\n')])

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(cleaned_body, 'html'))

    try:
        print(f"[DEBUG] Attempting to send email to {recipient_email} via {smtp_server}:{smtp_port}")
        with smtplib.SMTP(smtp_server, int(smtp_port)) as server:
            server.starttls()
            print(f"[DEBUG] STARTTLS established, attempting login for {sender_email}")
            server.login(sender_email, sender_password)
            print(f"[DEBUG] Login successful, sending message")
            server.send_message(msg)
            print(f"[DEBUG] Email sent successfully to {recipient_email}")
            return True
    except Exception as e:
        print(f"[ERROR] Failed to send email to {recipient_email}: {str(e)}")
        return False 