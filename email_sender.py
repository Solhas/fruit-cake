#!/usr/bin/env python3

from email.message import EmailMessage
import smtplib
import getpass

import debug_print

def send_email(from, to, subject, text, srvr_host, password):
    ### Compiles email from given data and attemts to send it. If exception is raised (no mail server configured/available) attempts to start new one locally

    # make message
    msg = EmailMessage()
    msg['From'] = from
    msg['To'] = to
    msg['Subject'] = Subject
    msg.set_content(text)

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
    s.send_email(msg)
