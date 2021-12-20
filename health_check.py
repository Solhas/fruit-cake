#!/usr/bin/env python3

import emails
import psutil
import socket
from time import sleep

#mail data

_LOCALHOST = "127.0.0.1"

#system limits in %
_CPU_THRESHOLD = 80
#_RAM_THRESHOLD = 70
_RAM = 500 * 1024 * 1024 # 500MB
_HDD_THRESHOLD = 80


# do the check
#check CPU, RAM and HDD usage
#get CPU load %
cpu_cores = psutil.cpu_count()
cpu_load = [x / cpu_cores * 100 for x in psutil.getloadavg()]
#get HDD usage %
disk = psutil.disk_usage("/")[3]
#get used RAM
mem = psutil.virtual_memory()

#ram_usage = mem.used / mem.total * 100.0

bad_disk = disk > _HDD_THRESHOLD
bad_ram = mem.available < _RAM

bad_net = False
try:
    adr = socket.gethostbyname("localhost")
    if adr != _LOCALHOST:
        bad_net = True
except:
    # failed to resolve, is bad
    bad_net = True
bad_cpu = False
for i in cpu_load:
    bad_cpu = bad_cpu or (i > _CPU_THRESHOLD)

print("CPU load, %: ", cpu_load)
print("RAM available: " + str(mem.available) + ", MB: " + str(mem.available / 1024 / 1024))
print("HDD available, %: " + str(100.0-disk))
if not bad_net:
    print("Localhost resolved as: ", adr)

#if bad
bad = bad_disk or bad_ram or bad_cpu or bad_net
if bad:
    if bad_cpu:
        subject = "Error - CPU usage is over 80%"
    if bad_disk:
        subject = "Error - Available disk space is less than 20%"
    if bad_ram:
        subject = "Error - Available memory is less than 500MB"
    if bad_net:
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
    text = "Please check your system and resolve the issue as soon as possible."
    msg = emails.generate_email2("automation@example.com", "student-00-d89ee86d8f06@example.com", subject, text)
    emails.send_email(msg)
