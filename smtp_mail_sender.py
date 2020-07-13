import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path #os.path is same

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'I am' #write your name your anything you want
email['to'] = 'i_am@somthing.com' #actual address
email['subject'] = 'Congratulations...'

email.set_content(html.substitute({'name': 'NIsarg'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port =587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('something@gamil.com','your_actual_passwoard')
    smtp.send_message(email)
    print("All done")
