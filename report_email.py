#!/usr/bin/env python3

from datetime import datetime
import os
import reports
import emails

_LOCATION = "/tmp/processed.pdf"
_SOURCE = "./supplier-data/descriptions/"

def main():
    data = []
    title = "Processed Update on " + datetime.now().strftime('%d-%m-%Y')
    for file in os.listdir(_SOURCE):
        with open(_SOURCE+file, 'r') as f:
            name = f.readline()
            weight = f.readline()
            new_entry = []
            new_entry.append("name: " + name)
            new_entry.append("weight: " + weight)
            data.append(new_entry)
    reports.generate_pdf(_LOCATION, title, data)

    subject = "Upload Completed - Online Fruit Store"
    text = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    msg = emails.generate_email("automation@example.com", "student-00-d89ee86d8f06@example.com", subject, text, "/tmp/processed.pdf")
    emails.send_email(msg)

if __name__ == "__main__":
    main()
