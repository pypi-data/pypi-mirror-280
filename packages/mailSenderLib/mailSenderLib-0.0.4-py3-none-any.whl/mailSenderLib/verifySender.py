# Developer settings
test_mode = False

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint

def getSMTPServer(mail_service: str):
    mail_service = mail_service.lower()
    if mail_service == 'gmail':
        return 'smtp.gmail.com', 587

class Message():
    def __init__(self, from_mail: str, from_password: str, to_mail: str, subject: str, text: str, to_name: str = ''):
        self.from_mail = from_mail
        self.from_password = from_password
        self.to_mail = to_mail
        self.to_name = to_name
        self.text = text
        self.subject = subject
    
    def send_verify_message(self, smtp_host: str, smtp_port: int):
        smtp = smtplib.SMTP(host=smtp_host, port=smtp_port)
        smtp.starttls()
        smtp.login(self.from_mail, self.from_password)
        
        message = MIMEMultipart()
        
        code = randint(100000, 999999)
        
        message['From'] = self.from_mail
        message['To'] = self.to_mail
        message['Subject'] = self.subject
        
        message.attach(MIMEText(self.text.format(self.to_name, code), 'plain'))
        smtp.send_message(message)
        del message
        
        smtp.quit()
        return code
        
if __name__ == '__main__':
    if test_mode:
        message = Message() # вставьте свои параметры
        host, port = getSMTPServer('gmail')
        message.send_verify_message(host, port)
        