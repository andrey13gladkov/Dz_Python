#3
def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""

    if number == 11 or number == 12 or number == 13 or number == 14:
        result = f'{number} процентов'
    elif number % 10 == 1:
        result = f'{number} процент'
    elif number % 10 == 2 or number % 10 == 3 or number % 10 == 4:
        result = f'{number} процента'
    else:
        result = f'{number} процентов'
    return result

for n in range(1, 101):
    print(transform_string(n))
