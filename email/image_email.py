#!/usr/bin/env python

import smtplib
import json


"""image_email.py sends a simple email with an image attachment"""

__author__ = "Ethan Ramchandani"

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

with open("/home/pi/.irpconfig") as config_file:
    config = json.load(config_file)

fromaddr = config['mail_account']
toaddr = config['alert_destination']
msg=MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "INtruder Alert"
filename = 'image.jpg'
attachment = open('image.jpg')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

body = "Intruder Alert"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login (fromaddr, config['mail_password'])
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()