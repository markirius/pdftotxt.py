import os
import sys
from pathlib import Path

try:
    import PyPDF2
except Exception as err:
    print(f'[!] use pip to install PyPDF2: {err}')


def convert_to_txt(pdf):
    pdffileobj = open(pdf, 'rb')
    pdfreader = PyPDF2.PdfFileReader(pdffileobj)
    filename = os.path.basename(pdf).split('.')[0]
    document = str(Path.home() / f'documents/{filename}.txt')
    for page in range(0, pdfreader.numPages):
        pageobj = pdfreader.getPage(page)
        text = pageobj.extractText()
        file = open(
                document,
                'a'
            )
        file.writelines(text)
    return document


if __name__ == '__main__':
    try:
        if sys.argv[1]:
            document = convert_to_txt(sys.argv[1])
            print(f'\ndocument was saved on {document}\n')
    except Exception as err:
        print(f'[!] an error occoured: {err}')
