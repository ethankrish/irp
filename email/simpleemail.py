#!/usr/bin/env python

import smtplib
import json

"""simpleemail.py sends an email with a simple image"""

__author__ = "Ethan Ramchandani"


with open("/home/pi/.irpconfig") as config_file:
    config = json.load(config_file)

fromaddr = config['mail_account']
toaddr = config['alert_destination']
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "INTRUDER ALERT"

body = "SOMEONE HAS TRIGGERED YOUR ALARM SYSTEM"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, config['mail_password']
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()