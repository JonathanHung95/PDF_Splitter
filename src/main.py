import os
from find_file.find_file import find_file
from split_pdf.split_pdf import split_pdf

root_dir = os.path.join(here)

input_dir = root_dir + "\\Input"
output_dir = root_dir + "\\Output"

file_list = find_file(input_dir)

