from dotenv import load_dotenv #pip install python-dotenv
import os

og_folder_path = ""
copy_folder_path = ""
file_extensions = []
file_enconding = ''

def load_parameters():
    load_dotenv()

    global og_folder_path 
    global copy_folder_path
    global file_extensions
    global file_enconding

    og_folder_path = os.getenv('og_folder_path')
    copy_folder_path = os.getenv('copy_folder_path')
    file_extensions = os.getenv('file_extensions')
    file_enconding = os.getenv('file_enconding')

    print(f'file_extensions: {file_extensions}')
    return

def check_hifen(og_line):
    if '-' in og_line:
        hifen_index = og_line.index('-')
        if og_line[hifen_index - 1] == og_line[hifen_index + 1]:
            idk_list = list(og_line)
            idk_list[hifen_index + 1] = idk_list[hifen_index + 1].lower()
            #TODO: Caso que não devia deixar no minusculo: 5300:[name]Takumi[line]“M-Misumi-kun... ?”[%p]
            return ''.join(idk_list)
    return og_line

def write_line(copy_file_path, og_line):

    f = open(copy_file_path, "a", encoding = file_enconding)
    new_line = check_hifen(og_line)
    # new_line = og_line
    f.write(new_line)
    f.close()

def create_one_file(copy_file_path):
    try:
        if os.path.isfile(copy_file_path):
            print(f'Overwriting {copy_file_path} file...')
        else:
            print(f'Creating {copy_file_path} file...')

        f = open(copy_file_path, "w", encoding = file_enconding)
        f.close()
    except:
        print(f'Error when creating file {copy_file_path}')

def read_one_file(og_folder_path, file_name):
    og_file_path = og_folder_path + "\\" + file_name
    print(f'Opening file {og_file_path}...')
    try:
        f = open(og_file_path, 'r', encoding = file_enconding)
        copy_file_path = f'{copy_folder_path}\\{file_name}'
        create_one_file(copy_file_path)
        for linha in f:
            write_line(copy_file_path, linha)
        f.close()
    except:
        print(f'Error when opening file {og_file_path}')

def is_valid_extension(file_name):
    for extension in file_extensions:
        if file_name.endswith(extension):
            return True
    return False

def read_files():
    for i in os.listdir(og_folder_path):

        if is_valid_extension(i):
            read_one_file(og_folder_path,i)


def main():
    load_parameters()
    read_files()

    #Tests:
    # copy_one_file(f'{copy_folder_path}\\idk.txt')
    # print(check_hifen('[name]Rintaro[line]"C-Claro."[%p]')) 
    # load_parameters()

main()