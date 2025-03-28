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
    smtp_port = int(os.environ.get("SMTP_PORT", 587))

    if not all([sender_email, sender_password, smtp_server]):
        print(f"[ERROR] Email server credentials are not fully configured.")
        print(f"SENDER_EMAIL: {'Set' if sender_email else 'Missing'}")
        print(f"SENDER_EMAIL_PASSWORD: {'Set' if sender_password else 'Missing'}")
        print(f"SMTP_SERVER: {'Set' if smtp_server else 'Missing'}")
        print(f"SMTP_PORT: {smtp_port}")
        return False

    # Clean up body text by removing leading spaces
    cleaned_body = "\n".join([line.strip() for line in body.split('\n')])

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(cleaned_body, 'html'))

    try:
        print(f"[DEBUG] Attempting to send email to {recipient_email} via {smtp_server}:{smtp_port}")
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
            
            # Send email
            server.send_message(msg)
            print(f"[DEBUG] Email sent successfully to {recipient_email}")
            
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
        print(f"[ERROR] SMTP Error: {str(e)}")
        return False
    except Exception as e:
        print(f"[ERROR] Failed to send email to {recipient_email}: {str(e)}")
        import traceback
        print(traceback.format_exc())
        return False 