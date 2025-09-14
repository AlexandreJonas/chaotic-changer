from dotenv import load_dotenv #pip install python-dotenv
import os

import create_logs

def load_parameters():
    load_dotenv()

    global og_folder_path 
    global copy_folder_path
    global file_extensions
    global file_enconding
    global debug_log_file_path
    global change_log_file_path
    global character_names_file_path
    global is_hifen
    global is_hifen_excecao
    global is_change_name
    global is_debug_log_txt

    og_folder_path = os.getenv('og_folder_path')
    copy_folder_path = os.getenv('copy_folder_path')
    file_extensions = os.getenv('file_extensions')
    file_enconding = os.getenv('file_enconding')
    debug_log_file_path = os.getenv('debug_log_file_path')
    change_log_file_path = os.getenv('change_log_file_path')
    character_names_file_path = os.getenv('character_names_file_path')

    is_hifen = ( os.getenv('is_hifen') == '1')
    is_hifen_excecao = ( os.getenv('is_hifen_excecao') == '1')
    is_change_name = ( os.getenv('is_change_name') == '1')
    is_debug_log_txt = ( os.getenv('is_debug_log_txt') == '1')

    return

def load_names():
    global all_names_list
    global full_names_list
    all_names_list = []
    full_names_list = []
    create_logs.debug_log(f'Loading names from file {character_names_file_path}...' )
    try:
        f = open(character_names_file_path, 'r', encoding = file_enconding)
        for line in f:
            #TODO: Refatorar lógica e nome de funções
            load_all_names(line)
            load_full_names(line)
        f.close()
    except:
        create_logs.debug_log(f'Error loading names from {character_names_file_path}')
    return

def load_all_names(line):
    global all_names_list
    separated_name = line.split()
    for single_name in separated_name:
        all_names_list.append(single_name.replace("\n",""))
    return

def load_full_names(line):
    global full_names_list
    separated_name = line.split()

    if len(separated_name) > 1:
        full_names_list.append(line.replace("\n",""))
    return 