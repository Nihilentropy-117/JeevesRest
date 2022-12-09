import datetime
import email
import imaplib
from smtplib import SMTP_SSL, SMTP_SSL_PORT


def open_connection(credentials):
    connection = imaplib.IMAP4_SSL(credentials["imap"])
    connection.login(credentials["username"], credentials["password"])
    print("Opening Connection")
    return connection

def sendMail(credentials, to, subject, body):
    SMTP_HOST = credentials["smtp"]
    SMTP_USER = credentials["username"]
    SMTP_PASS = credentials["password"]
    from_email = credentials["username"]
    to_emails = [to]

    # Build Headers
    headers = f"From: {from_email}\r\n"
    headers += f"To: {', '.join(to_emails)}\r\n"
    headers += f"Subject: {subject}\r\n"

    # Assemble Message
    email_message = headers + "\r\n" + body

    # Connect and Login to SMTP, then send
    smtp_server = SMTP_SSL(SMTP_HOST, port=SMTP_SSL_PORT)
    # smtp_server.set_debuglevel(0)  # SMTP Debug
    smtp_server.login(SMTP_USER, SMTP_PASS)
    smtp_server.sendmail(from_email, to_emails, email_message)

    # Disconnect
    smtp_server.quit()