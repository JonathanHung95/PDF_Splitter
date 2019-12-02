import os

def find_file(input_dir):
    """
    Obtain a list of files from the input_dir that need to be split.
    
    :param input_dir: Path to the input directory.
    
    :return: File name.
    """

    file_list = []
    
    for f in os.listdir(input_dir):
        if f.endswith(".pdf"):
            file_list.append(f)
    
    return file_list