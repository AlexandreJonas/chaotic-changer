import parameters
import create_logs

def load_names():
    global all_names_list
    global full_names_list
    all_names_list = []
    full_names_list = []
    create_logs.debug_log(f'Loading names from file {parameters.character_names_file_path}...' )
    try:
        f = open(parameters.character_names_file_path, 'r', encoding = parameters.file_enconding)
        for line in f:
           all_names_list.append(line.replace("\n",""))
           load_full_names(line)
        f.close()
    except:
        create_logs.debug_log(f'Error loading names from {parameters.character_names_file_path}')
    return


def load_full_names(line):
    global full_names_list
    separated_name = line.split()

    if len(separated_name) > 1:
        full_names_list.append(line.replace("\n",""))
    return 