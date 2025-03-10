import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "zigmarszigmars19@gmail.com"
password = "rygl culp blcc smky"

receiver = "zigmarszigmars19@gmail.com"


context = ssl.create_default_context()
message = f"""\
From: {username}
To: {receiver}
Subject: Portfolio Contact Me

Hi, how high are you?
"""


with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password) # login as the user of the account
    server.sendmail(username, receiver, message)
