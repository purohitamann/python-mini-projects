import PyPDF2
import sys
import os
from docx import Document


def merge_pdf_files(pdf1,pdf2):
    merger = PyPDF2.PdfMerger()
    if not os.path.isfile(pdf1):
        print(f"File {pdf1} does not exist.")
        sys.exit(1)

    if not os.path.isfile(pdf2):
        print(f"File {pdf2} does not exist.")
        sys.exit(1)

    dir1= os.path.dirname(pdf1)
    dir2= os.path.dirname(pdf2)
    dir='/Users/amanpurohit/Desktop/PROJECTS/python-mini-projects/pdfMerger'
    if dir1 == dir2:
        dir=dir1
    else:
     dir =input('Please provide pdfs from same directory (absolute path): ')   
    filename1= os.path.basename(pdf1)[:4]
    filename2= os.path.basename(pdf2)[:4]
    filename = filename1 +'-'+ filename2 + '-merged'+'.pdf'
    print(f' Registered location for \n \t pdf 01 loaction: {dir} \n \t pdf 02 loaction: {dir2}');
    # for file in os.listdir(os.curdir):
    if pdf1.endswith('.pdf') and pdf2.endswith('.pdf'):
        merger.append(pdf1)
        merger.append(pdf2)
        
    merger.write(os.path.join(dir,filename))
    print(f'Merged {pdf1.title()} and {pdf2.title()} into {filename}.pdf \n path: {os.path.abspath(filename)}')
    merger.close()


def merge_docx_files(docx1, docx2):
   
    if not os.path.isfile(docx1):
        print(f"File {docx1} does not exist.")
        sys.exit(1)

    if not os.path.isfile(docx2):
        print(f"File {docx2} does not exist.")
        sys.exit(1)
    # for file in os.listdir(os.curdir):
    merger_for_docx(docx1, docx2)

def merger_for_docx(docx1, docx2):
    doc1 = Document(docx1)
    doc2 = Document(docx2)
    
    dir1= os.path.dirname(docx1)
    dir2= os.path.dirname(docx2)
    dir='/Users/amanpurohit/Desktop/PROJECTS/python-mini-projects/pdfMerger'
    if dir1 == dir2:
        dir=dir1
    else:
     dir =input('Please provide pdfs from same directory (absolute path): ') 
    filename1= os.path.basename(docx1)[:4]
    filename2= os.path.basename(docx2)[:4]
    filename = filename1 +'-'+ filename2 + '-merged'+'.docx'
    print(f' Registered location for \n \t pdf 01 loaction: {dir} \n \t pdf 02 loaction: {dir2}')
    for element in doc2.element.body:
        doc1.element.body.append(element)
    
    doc1.save(filename)
    print(f'Merged {docx1.title()} and {docx2.title()} into {filename}.docx \n path: {os.path.abspath(filename)}')
# Docx files merging
merge_docx_files(['/path/to/doc1.docx', '/path/to/doc2.docx'], 'merged.docx')

# Pdf files merging
pdf1 = sys.argv[1]
pdf2 = sys.argv[2]

# merge_pdf_files(pdf1, pdf2)
merge_docx_files(pdf1, pdf2)