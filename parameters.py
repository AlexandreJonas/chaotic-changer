from dotenv import load_dotenv #pip install python-dotenv
import os

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

    return