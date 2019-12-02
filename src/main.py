import os
from find_file.find_file import find_file
from split_pdf.split_pdf import split_pdf

root_dir = os.path.join(here)

input_dir = root_dir + "\\Input"
output_dir = root_dir + "\\Output"

file_list = find_file(input_dir)

for f in file_list:
    file_path = input_dir + "\\" + f
    
    split_pdf(file_path, f, output_dir)
    print("Deleting " + f)
    os.remove(file_path)
    