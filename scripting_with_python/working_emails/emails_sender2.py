import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('./scripting_with_python/working_emails/index.html').read_text())
email = EmailMessage()
email['from'] = 'Andrei Neagoie'
email['to'] = 'prakharguptap982@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('prakharankita982@gmail.com', 'aezakmio')
  smtp.send_message(email)
  print('all good boss!')