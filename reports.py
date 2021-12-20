#!/usr/bin/env python3
from datetime import datetime
import os
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer, Table, Image

def generate_pdf(filename, title, data):
    ### Compiles pdf from list[list[line]] and writes to filename
    styles = getSampleStyleSheet()
    pdf_compile = []
    blank = Spacer(0, 12)
    pdf_compile.append(Paragraph(title, styles['h1']))
    for p in data:
        for entry in p:
            next_block = Paragraph(entry, styles['Normal'])
            pdf_compile.append(next_block)
        pdf_compile.append(blank)

    report = SimpleDocTemplate(filename)
    report.build(pdf_compile)
