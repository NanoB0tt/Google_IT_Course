#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def gen_report(filename, title, data):
    style = getSampleStyleSheet
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, style["h1"]
    report_data = Paragraph(data, style["BodyText"])
    empty_line = Spacer(1,20)

    report.build([report_title, empty_line, report_data, empty_line])

