vocab_eng_rus = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
    'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(eng_word):
    return vocab_eng_rus.get(eng_word)


print(num_translate('five'))
print(num_translate('nine'))