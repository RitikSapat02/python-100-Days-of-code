
def format_name(f_name,l_name):
    '''This is a function which will convert first name and last name to title case'''

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"


print(format_name("angela","AnGelA"))


'''
multiline comment:

it is a turn arround to create multiline comment because if we does not assign  any triple coted string to any variable it will be ignored .
note that multipline comments like this are not recommended beacuse we get confuse it with docstring
'''
