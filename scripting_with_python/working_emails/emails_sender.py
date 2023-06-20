import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Prakhar Gupta'
email['to'] = 'prakharguptap982@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content('I am a Python Master!!')

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("prakharankita982@gmail.com", "aezakmio")
    smtp.ehlo()
    #smtp.sendmail("prakharankita982@gmail.com", "prakharguptap982@gmail.com", email)
    smtp.send_message(email)
    print('All good boss!')