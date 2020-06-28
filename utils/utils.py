def del_all_spaces(string):
    spaces = '\t\n '
    buff = ''
    for letter in string:
        if letter not in spaces:
            buff += letter
    return buff

