#!/usr/bin/env python3

from email.message import EmailMessage
import os
import mimetypes
import smtplib
import getpass

_MAIL_SERVER = "localhost"
_MAIL_PWD = "n6cP5Yh8yFC"
_MAIL_I = "me"

def generate_email(frm, to, subject, text, attachment):
    msg = compile_email(frm, to, subject, text)
    msg = add_file(msg, attachment)
    return msg

def generate_email2(frm, to, subject, text):
    msg = compile_email(frm, to, subject, text)    
    return msg


def send_email(email):
    srvr_host = _MAIL_SERVER
    password = _MAIL_PWD
    ### Attempts to send email via given credentials. Fails if no mail server configured/available

    # attempt to access mail server at srvr_host
    try:
        s = smtplib.SMTP(srvr_host)

    except ConnectionRefusedError as e:
        print("No server available at {}, for details see {}".format(srvr_host, e))
        print("Attempting to DO WHAT EXACTLY? NOT IMPLEMENTED")
        print("Message delivery failed")

    #login & send
    try:
        pwd = getpass.getpass(password)
        s.login(frm, pwd)
    except:
        #do nothing... :(
        print("Login failed")
    s.send_message(email)
    print("Mail sent succesfully")

# construct email object
# requires sender, reciever, subject and text
def compile_email(frm, to, subject, text):
    msg = EmailMessage()
    msg['From'] = frm
    msg['To'] = to
    msg['Subject'] = subject
    msg.set_content(text)
    return msg

# guesses mime type of attachment and adds it to existing email
def add_file(msg, attach):
    m_type, _ = mimetypes.guess_type(attach)
    m_type, m_subtype = m_type.split('/', 1)
    with open(attach, 'rb') as ap:
        msg.add_attachment(ap.read(), maintype = m_type, subtype = m_subtype, filename = os.path.basename(attach))
    return msg
