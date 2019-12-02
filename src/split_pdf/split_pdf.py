import os
from PyPDF2 import PdfFileReader, PdfFileWriter

def split_pdf(file_path, file_name, output_dir):
    """
    Split the pdf into smaller pdfs and write to the Output folder.
    
    :param file_path: File path of the pdf file.
    :param file_name: Name of the pdf file.
    :param output_dir: Path to the output directory.
    
    :return: None.
    """
    
    pdf = PdfFileReader(file_path)
    
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        
        output_filename = "{}_page_{}.pdf".format(file_name, page + 1)
        
        with open(output_dir + "\\" + output_filename, "wb") as out:
            pdf_writer.write(out)
            
        print("Created: {}".format(output_filename))
        
    return None