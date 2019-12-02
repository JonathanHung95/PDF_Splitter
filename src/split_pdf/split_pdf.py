import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def split_pdf(file_name):
    """
    Split the pdf into smaller pdfs and write to the Output folder.
    
    :param:
    
    :return: None.
    """
    
    os.path.abspath(os.curdir)
    file_path = os.chdir("..")    
    
    file_path = file_path.format
    
    pdf = PdfFileReader(file_path)
    
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        
        output_filename = "{}_page_{}.pdf".format(file_name, page + 1)
        
        with open(output_filename, "wb") as out:
            pdf_writer.write(out)
            
        print("Created: {}".format(output_filename))
        
    return None