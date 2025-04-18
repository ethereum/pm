import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_email(recipient_emails, subject, body):
    """
    Send an email to the recipient(s) with the given subject and body.
    
    Args:
        recipient_emails: A list of email addresses for the recipients.
        subject: Email subject line
        body: HTML body content of the email
    
    Returns:
        bool: True if email was sent successfully to all recipients, False otherwise
    """
    sender_email = os.environ.get("SENDER_EMAIL")
    sender_password = os.environ.get("SENDER_EMAIL_PASSWORD")
    smtp_server = os.environ.get("SMTP_SERVER")
    smtp_port = int(os.environ.get("SMTP_PORT", 587))

    if not all([sender_email, sender_password, smtp_server]):
        print(f"[ERROR] Email server credentials are not fully configured.")
        print(f"SENDER_EMAIL: {'Set' if sender_email else 'Missing'}")
        print(f"SENDER_EMAIL_PASSWORD: {'Set' if sender_password else 'Missing'}")
        print(f"SMTP_SERVER: {'Set' if smtp_server else 'Missing'}")
        print(f"SMTP_PORT: {smtp_port}")
        return False

    # Ensure recipient_emails is a list
    if isinstance(recipient_emails, str):
        recipient_emails = [recipient_emails] # Convert single email string to list

    if not recipient_emails:
         print("[ERROR] No recipient emails provided.")
         return False

    # Clean up body text by removing leading spaces
    cleaned_body = "\n".join([line.strip() for line in body.split('\n')])

    msg = MIMEMultipart()
    msg['From'] = sender_email
    # Join the list of emails into a comma-separated string for the 'To' header
    msg['To'] = ", ".join(recipient_emails) 
    msg['Subject'] = subject

    msg.attach(MIMEText(cleaned_body, 'html'))

    recipients_str = ", ".join(recipient_emails) # For logging

    try:
        print(f"[DEBUG] Attempting to send email to {recipients_str} via {smtp_server}:{smtp_port}")
        server = None
        
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            # Disable debug output
            server.set_debuglevel(0)
            
            # Start TLS for security
            server.starttls()
            print(f"[DEBUG] STARTTLS established, attempting login for {sender_email}")
            
            # Authentication
            server.login(sender_email, sender_password)
            print(f"[DEBUG] Login successful, sending message")
            
            # Send email to all recipients in the list
            server.send_message(msg, sender_email, recipient_emails) 
            print(f"[DEBUG] Email sent successfully to {recipients_str}")
            
            return True
        finally:
            # Make sure to quit the server even if an error occurs
            if server:
                server.quit()
                print("[DEBUG] SMTP connection closed")
    except smtplib.SMTPAuthenticationError as e:
        print(f"[ERROR] SMTP Authentication Error - Check your email credentials: {str(e)}")
        return False
    except smtplib.SMTPConnectError as e:
        print(f"[ERROR] SMTP Connection Error - Could not connect to SMTP server: {str(e)}")
        return False
    except smtplib.SMTPServerDisconnected as e:
        print(f"[ERROR] SMTP Server Disconnected: {str(e)}")
        return False
    except smtplib.SMTPException as e:
        # Includes potential smtplib.SMTPRecipientsRefused if the server rejects one or more recipients
        print(f"[ERROR] SMTP Error sending to {recipients_str}: {str(e)}") 
        return False
    except Exception as e:
        print(f"[ERROR] Failed to send email to {recipients_str}: {str(e)}")
        import traceback
        print(traceback.format_exc())
        return False 