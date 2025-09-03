import parameters

def debug_log(debug_message):
    debug_log_file_path = parameters.debug_log_file_path
    f = open(debug_log_file_path, "a", encoding = 'utf-8')
    f.write(debug_message)
    f.write('\n')
    f.close()
    return


def change_log(filename, line_number, og_line,new_line):
    change_log_file_path = parameters.change_log_file_path
    og_line = og_line.replace('\n','')
    new_line = new_line.replace('\n','')
    f = open(change_log_file_path, "a", encoding = 'utf-8')
    csv_log = f'{filename};{line_number};{og_line};{new_line}'
    f.write(csv_log)
    f.write('\n')
    f.close()
    return