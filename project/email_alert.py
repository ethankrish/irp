#!/usr/bin/env python

import logging
import smtplib


"""email_alert sends an email with an image attachment"""

__author__ = "Ethan Ramchandani"


from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

import config
from internetcheck import internet_on


def send_email(to, subject, body, img):
    try:
        if not internet_on():
            logging.debug("Not connected to internet")
            return
        config.initialize()
        fromaddr = config.get_value('mail_account')
        toaddr = to
        msg=MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = subject
        filename = img
        attachment = open(img)
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login (fromaddr, config.get_value('mail_password'))
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
    except:
        logging.exception("Error sending email")

if __name__ == '__main__':
    send_email('mahesh.ramchandani@gmail.com', 'Testing', 'Hello world', 'image.jpg')
