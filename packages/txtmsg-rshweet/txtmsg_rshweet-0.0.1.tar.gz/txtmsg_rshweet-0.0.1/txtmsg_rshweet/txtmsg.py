import smtplib
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context
import email
from utilities_pkg.txtmsg_pkg.providers import PROVIDERS 
from utilities_pkg.txtmsg_pkg.exceptions import (
    ProviderNotFoundException,
    NumberNotValidException
)

class SendTxtMsg:
    "returns a dataframe with 40 option prices (DTE) for each type (C and P) based on an input strike and price (from event_trigger.symbol_df )  "
    def __init__(self, message:str, subject:str="Sent from Python", provider:str="Verizon", phone_number:str="2088504993", 
                 smtp_server:str="smtp.gmail.com", smtp_port:int=465):
        self.number = phone_number 
        valid = False
        num = ""
        for character in self.number:
            if character.isdigit():
                num += character
        # a phone number will have a valid length of 10 digits as all of the phone
        # domains are US phone domains with area codes
        if len(num) == 10:
            valid = True
        if not valid:
            raise NumberNotValidException(self.number)

        self.message = message
        self.provider = provider
        provider_info = PROVIDERS.get(provider)
        if provider_info == None:
            raise ProviderNotFoundException(provider)

        self.domain = provider_info.get("sms")
        self.sender_email, self.email_password = ('rshcode1@gmail.com', 'vhps mekx zkjr msur')
        self.receiver_email = f"{num}@{self.domain}"
        self.subject=subject 
        self.smtp_server=smtp_server
        self.smtp_port=smtp_port
        self.email_message = f"Subject: {self.subject}\nTo:{self.receiver_email}\n{self.message}"

    def send_sms_via_email(self):
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port, context=ssl.create_default_context()) as email:
            email.login(self.sender_email, self.email_password)
            email.sendmail(self.sender_email, self.receiver_email, self.email_message)