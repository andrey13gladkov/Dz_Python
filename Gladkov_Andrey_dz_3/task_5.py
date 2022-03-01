import random


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(number):
    """Реализация функции get_jokes"""
    list_1 = []
    for a in range(number):
        noun = random.choice(nouns)
        adv = random.choice(adverbs)
        adj = random.choice(adjectives)
        list_1.append(f'{noun} {adv} {adj}')
    return list_1

print(get_jokes(1))
print(get_jokes(2))
print(get_jokes(3))

def get_joke_adv(number, repeats=True):
    list_1 = []
    if not repeats:
        if number > min(len(nouns), len(adverbs), len(adjectives)):
            return "Impossible"
        else:
            random.shuffle(nouns)
            random.shuffle(adverbs)
            random.shuffle(adjectives)
            for a in range(number):
                list_1.append(f'{nouns[a]} {adverbs[a]} {adjectives[a]}')
    else:
        for a in range(number):
            noun = random.choice(nouns)
            adv = random.choice(adverbs)
            adj = random.choice(adjectives)
            list_1.append(f'{noun} {adv} {adj}')
    return list_1

print(get_joke_adv(4, False))
print(get_joke_adv(5, False))
print(get_joke_adv(6, False))