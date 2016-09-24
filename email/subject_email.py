import smtplib
import json
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

with open("/home/pi/.irpconfig") as config_file:
    config = json.load(config_file)

fromaddr = config['mail_account']
toaddr = config['alert_destination']
msg=MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "INtruder Alert"

body = "Intruder Alert"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login (fromaddr, config['mail_password'])
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()