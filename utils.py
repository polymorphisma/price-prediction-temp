import os


data_dir = r'data/stockwise'
special_character = ['-', '/']


def generate_file(directory, file_name):
    for char in special_character:
        if char in file_name:
            file_name = file_name.replace(char, '_')
    file_path = os.path.join(directory, file_name+'.csv')
    return file_path


def return_files(path: str, full_path: bool = True):
    if full_path:
        return [os.path.join(path, x) for x in os.listdir(path)]
    return [x for x in os.listdir(path)]
