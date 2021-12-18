#!/usr/bin/env python3

import os
import reporter
import email_sender

_TITLE = "Uploaded data report"
_REPORT_FILE = "report.pdf"

_MAIL_TO = "supplier"
_MAIL_TEXT = "Uploaded data report in attachment"

def load_data():
    pass

def upload_desc(pic):
    pass

def upload_pic(desc):
    pass

def main():
    data = load_data()
    report_data = []
    for pic, desc in data:
        upload_pic(pic)
        upload_desc(desc)
        report_data.append("Uploaded " + pic + " : " desc)
    pdf_compile = []
    pdf_compile.append(_TITLE_, 'Heading1')
    for x in report_data:
        pdf_compile.append(x, 'Normal')
    reporter.build_pdf(_REPORT_FILE_), pdf_compile)
    email_sender.send_byme_attach(_MAIL_TO, _TITLE, _MAIL_TEXT, _REPORT_FILE)

if __name__ == "__main__":
    sys.exit(main())
