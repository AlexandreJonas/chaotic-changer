from dotenv import load_dotenv #pip install python-dotenv
import os

from create_logs import *
import parameters
import change_name

#TODO: Renomear função para ficar mais descritivo
#Função para verificar se a palavra a ser alterada não está na lista de nomes
def is_lower_word(og_line, hifen_index):
  
    if not parameters.is_hifen_excecao:
        return True
    after_hifen_str = og_line[hifen_index + 1:]
    for name in parameters.all_names_list:
        if name in after_hifen_str:
            name_index = after_hifen_str.index(name)
            if name_index < 1:
                return False
    return True

def check_hifen(og_line):
    #TODO: Refatorar lógica
    if parameters.is_hifen and  ('-' in og_line) :
        hifen_index = og_line.index('-')
        if not is_lower_word(og_line, hifen_index):
            return og_line
        if og_line[hifen_index - 1] == og_line[hifen_index + 1]:
            idk_list = list(og_line)
            idk_list[hifen_index + 1] = idk_list[hifen_index + 1].lower()
            return ''.join(idk_list)
    return og_line

def write_line(copy_file_path, og_line, line_number):

    f = open(copy_file_path, "a", encoding = parameters.file_enconding)
    new_line = check_hifen(og_line)
    new_line = change_name.check_change_name(new_line)
    f.write(new_line)
    f.close()

    if not new_line == og_line:
        change_log(copy_file_path,line_number,og_line,new_line)

def create_one_file(copy_file_path):
    try:
        if os.path.isfile(copy_file_path):
            debug_log(f'Overwriting {copy_file_path} file...')
        else:
            debug_log(f'Creating {copy_file_path} file...')

        f = open(copy_file_path, "w", encoding = parameters.file_enconding)
        f.close()
    except:
        debug_log(f'Error when creating file {copy_file_path}')

def read_one_file(file_name):
    og_file_path = parameters.og_folder_path + "\\" + file_name
    line_number = 0
    debug_log(f'Opening file {og_file_path}...' )
    try:
        f = open(og_file_path, 'r', encoding = parameters.file_enconding)
        copy_file_path = f'{parameters.copy_folder_path}\\{file_name}'
        create_one_file(copy_file_path)
        for linha in f:
            line_number += 1
            write_line(copy_file_path, linha,line_number)
        f.close()
    except:
        debug_log(f'Error when opening file {og_file_path}')

def is_valid_extension(file_name):
    for extension in parameters.file_extensions:
        if file_name.endswith(extension):
            return True
    return False

def read_files():
    for i in os.listdir(parameters.og_folder_path):

        if is_valid_extension(i):
            read_one_file(i)


def main():
    parameters.load_parameters()
    parameters.load_names()
    change_log('Nome do Arquivo', 'Número da Linha', 'Linha Original', 'Linha Alterada')
    read_files()

    #Tests:
    # print(check_hifen('[name]Rintaro[line]"C-Claro."[%p]')) 
    # debug_log('YAY')
    # print( is_lower_word('5300:[name]Takumi[line]“M-Misumi-kun... ?”[%p]',25)  )
    # print( is_lower_word('5300:[name]Takumi[line]“B-Batata-kun  Misumi... ?”[%p]',25)  )
    # print( change_name.check_change_name("something something rintAro okabe") )

main()