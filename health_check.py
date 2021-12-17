#!/usr/bin/env python3

import email_sender
import psutil
from time import sleep

#mail data
_MAIL_SERVER = "mail.stub.net"
_MAIL_PWD = "qwertypass"
_MAIL_FROM = "me"
_MAIL_TO = "you"
#mail templates
_MAIL_SUBJECT = "System health alert"
_MAIL_MSG_TEMPLATE = "Bad stuff be happenin at {}"

#script check timeout
_TIMEOUT = 5
#system limits in %
_CPU_THRESHOLD = 70
_RAM_THRESHOLD = 70
_HDD_THRESHOLD = 70


def system_checker():
### checks system health and sends email if things bad
    # do the check
    while True:
        #check CPU, RAM and HDD usage

        #get CPU load %
        cpu_cores = psutil.cpu_count()
        cpu_load = [x / cpu_cores * 100 for x in psutil.getloadavg()]
        #get HDD usage %
        disk = psutil.disk_usage()[3]
        #get used RAM %
        mem = psutil.virtual_memory()
        ram_usage = mem.used / mem.total * 100.0

        bad = (disk > _HDD_THRESHOLD) or (ram_usage > _RAM_THRESHOLD)
        for i in cpu_load:
            bad = bad or (i > _CPU_THRESHOLD)
        #if bad
        if bad:
            where = "here"
            email_sender.send_email(_MAIL_FROM, _MAIL_TO, _MAIL_SUBJECT, _MAIL_MSG_TEMPLATE.format(where))
            break
        sleep(_TIMEOUT)
