#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer, Table, Image

# Compiles pdf from tuple list and writes to filename
# Expected typle format for data: (text_string, style_name)
def build_pdf(filename, data):
    styles = getSampleStyleSheet()
    pdf_compile = []
    blank = Spacer(1,0.2*inch)
    for p in data:
        next_block = Paragraph(p[0], styles[p[1]])
        pdf_compile.append(next_block)
        pdf_compile.append(blank)
    report = SimpleDocTemplate("/tmp/report.pdf")
    report.build(pdf_compile)
