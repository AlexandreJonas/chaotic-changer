import parameters
import create_logs

def check_change_name(og_line):
    if not parameters.is_change_name:
        return og_line
    
    for full_name in parameters.full_names_list:
        split_name_list = full_name.split()
        inverted_incorrect_name = f'{split_name_list[1]} {split_name_list[0]}'

        if inverted_incorrect_name.lower() in og_line.lower() :
            incorrect_name_index = og_line.lower().index(inverted_incorrect_name.lower())
            incorrect_name_len = len(inverted_incorrect_name)
            aux_str = og_line[incorrect_name_index: incorrect_name_index + incorrect_name_len]
            changed_name = og_line.replace(aux_str,full_name)
            return changed_name
    return og_line