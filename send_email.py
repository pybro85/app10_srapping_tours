import smtplib, ssl
from email.message import EmailMessage
import os


def send_email():
    email_message = EmailMessage()
    email_message["Subject"] = "New event has been assigned!"
    email_message.set_content("Heads up, we've got a new event announcement for you")
    host = "smtp.gmail.com"
    port = 465

    username = "kartalcarriers@gmail.com"
    password = "fshudcdrvqkczvof"

    receiver = "kartalcarriers@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, email_message.as_string())
    print("Email was sent")
