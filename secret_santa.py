import random


def secret_santa(spisok):
    shuffled_uchastniki = list(spisok)
    random.shuffle(shuffled_uchastniki)
    for i in range(len(spisok)):
        if spisok[i] != shuffled_uchastniki[i]:
            continue
        else:
            r = shuffled_uchastniki.pop(i)
            shuffled_uchastniki.append(r)
    a = {spisok[i]: shuffled_uchastniki[i] for i in range(len(spisok))}
    return a


uchastniki = ['Алексей Мочалов', 'Александр Бабенков', 'Дарья Самосадова', 'Юлия Баширова', 'Валерия Бабенкова',
              'Алексей Самосадов', 'Дарья Соседка']
res = secret_santa(uchastniki)
for key, value in res.items():
    print(f'{key} -> {value}')
