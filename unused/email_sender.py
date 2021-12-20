#!/usr/bin/env python3

from email.message import EmailMessage
import os
import mimetypes
import smtplib
import getpass

_MAIL_SERVER = "mail.stub.net"
_MAIL_PWD = "qwertypass"
_MAIL_I = "me"

def send_byme(to, subject, text):
    ### sends email with default sender, mail server and password
    send_email(_MAIL_I, to, subject, text, _MAIL_SERVER, _MAIL_PWD)

def send_byme_attach(to, subject, text, attach):
    ### sends email w attachment with default sender, mail server and password
    send_email_attached(_MAIL_I, to, subject, text, attach, _MAIL_SERVER, _MAIL_PWD)

def send_email_attached(from, to, subject, text, attach, srvr_host, password):
    ### Compiles email from given data, adds attachment and attemts to send it.

    # make message
    msg = compile_email(from, to, subject, text)
    #add attachment
    msg = add_file(msg, attach)
    # attempt to access mail server at srvr_host
    actually_send(msg, srvr_host, password)


def send_email(from, to, subject, text, srvr_host, password):
    ### Compiles email from given data and attemts to send it.

    # make message
    msg = compile_email(from, to, subject, text)
    # attempt to access mail server at srvr_host
    actually_send(msg, srvr_host, password)

def actually_send(email, srvr_host, password):
    ### Attempts to send email via given credentials. Fails if no mail server configured/available

    # attempt to access mail server at srvr_host
    try:
        s = smtplib.SMTP(srvr_host)

    except ConnectionRefusedError as e:
        print("No server available at {}, for details see {}".format(srvr_host, e))
        print("Attempting to DO WHAT EXACTLY? NOT IMPLEMENTED")
        print("Message delivery failed")

    #login & send
    pwd = getpass.getpass(password)
    s.login(from, pwd)
    s.send_email(email)

# construct email object
# requires sender, reciever, subject and text
def compile_email(from, to, subject, text):
    msg = EmailMessage()
    msg['From'] = from
    msg['To'] = to
    msg['Subject'] = Subject
    msg.set_content(text)
    return msg

# guesses mime type of attachment and adds it to existing email
def add_file(msg, attach):
    m_type, _ = mimetypes.guess_type(attach)
    m_type, m_subtype = mime_type.split('/', 1)
    with open(attach, 'rb') as ap:
        msg.add_attachment(ap.read(), maintype = m_type, subtype = m_subtype, filename = os.path.basename(attach))
    return msg
