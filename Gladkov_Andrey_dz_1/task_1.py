#1 задание
def convert_time(duration: int) -> str:
    days = duration // 86400
    seconds = duration % 86400 % 3600 % 60
    minutes = duration % 86400 % 3600 // 60
    hours = duration % 86400 // 3600

    if duration >= 86400:
        time = '{} дн {} час {} мин {} сек'.format(days, hours, minutes, seconds)
    elif duration >= 3600:
        time = '{} час {} мин {} сек'.format(hours, minutes, seconds)
    elif duration >= 60:
        time = '{} мин {} сек'.format(minutes, seconds)
    else:
        time = '{} сек'.format(seconds)
    return time


duration = 5748586
result = convert_time(duration)
print(result)
