from random import uniform

#a
def transfer_list_in_str(list_in: list) -> str:
    str_out = ''
    for n in range(len(list_in)):
        if n != len(list_in) - 1:
            rub = int(list_in[n])
            kop = str(list_in[n])[str(list_in[n]).index('.') + 1:]
            if len(kop) < 2:
                kop = '0' + kop
                str_out += ('%d руб %s коп,' % (rub, kop))
            elif n == len(list_in) - 1:
                rub = int(list_in[n])
                kop = list_in[n] * 100 % 100
                str_out += ('%s руб %d коп' % (rub, kop))
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)
id_my_list = id(my_list)
print('\n')


#b

def sort_prices(list_in: list) -> list:
    list_in.sort()
    return list_in

result_2 = sort_prices(my_list)
print(result_2)
id_sorted_my_list = id(result_2)
if id_sorted_my_list == id_my_list:
    print('Не поменялся')
print('\n')


#c

def sort_price_adv(list_in: list) -> list:
    list_out = sorted(list_in)
    list_out.reverse()
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)
print('\n')


#d

def check_five_max_elements(list_in: list) -> list:
    list_out = []
    sort_list = sort_price_adv(list_in)
    for n in range(5):
        list_out.append(sort_list[n])
    return list_out

result_4 = check_five_max_elements(my_list)
print(result_4)
