def convert_list_in_str(list_in: list) -> str:
    i_list = []
    for home_str in list_in:
        if home_str.isdigit():
            home_str = int(home_str)
            i_list.append(f'"{home_str:02d}"')
        elif home_str[0] == '+':
            home_str = int(home_str[1:])
            i_list.append(f'"+{home_str:02d}"')
        elif home_str[0] == '-':
            home_str = int(home_str[1:])
            i_list.append(f'"-{home_str:02d}"')
        else:
            i_list.append(home_str)
        str_out = ''.join(i_list)
        return  str_out

    my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
    result = convert_list_in_str(my_list)
    print(result)