import os

from markdown import markdown
import pdfkit

from config import CONTENT_DIR


def create_pdf(pdf_data):
    input_filename = ''
    output_filename = ''

    with open(pdf_data, 'r') as f:
        html_text = markdown(f.read(), output_format='html4')

    pdfkit.from_string(html_text, output_filename)

    #os.path.exists(filename)

