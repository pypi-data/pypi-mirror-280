import smtplib
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

class SendEmailMsg:
    def __init__(self, message:str, subject:str, receiver_email:str, smtp_server:str, smtp_port:int, sender_email:str, sender_email_password:str):

        self.message = message

        self.sender_email = sender_email
        self.email_password = sender_email_password
        self.receiver_email = receiver_email
        self.subject=subject 
        self.smtp_server=smtp_server
        self.smtp_port=smtp_port
        self.email_message = f"Subject: {self.subject}\nTo:{self.receiver_email}\n{self.message}"

    def send_email(self):
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=ssl.create_default_context()) as email:
            email.login(self.sender_email, self.email_password)
            email.sendmail(self.sender_email, self.receiver_email, self.email_message)