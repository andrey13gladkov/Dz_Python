def convert_name_extract(list_in: list) -> list:
    for n in range(len(list_in)):
        list_in[n] = list_in[n].split()
        list_in[n] = f"Привет, {list_in[n][-1].lower().title()}!"
    return list_in

my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)