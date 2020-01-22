import smtplib
from email.message import EmailMessage
from string import Template #to have a parametric content
from pathlib import Path    


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Hilal'
email['to'] = 'the.ihlal.84@gmail.com'
email['subject'] = 'You won a million dollars!'

# email.set_content('I am a python master!')  # TEXT based email
# email.set_content(html.substitute(name='Hilal')) # single variable
# email.set_content(html.substitute({'name':'Hilal', 'age':'35'})) # multiple variables
email.set_content(html.substitute({'name': 'Hilal'}), 'html') # we give html as parameter to set content as an html

with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp:
  smtp.ehlo()
  smtp.starttls() # encryption mechanism
  smtp.login('the.ihlal.84@gmail.com', 'ffqbwfaucjudcpcy')
  smtp.send_message(email)
  print('all good boss!')



