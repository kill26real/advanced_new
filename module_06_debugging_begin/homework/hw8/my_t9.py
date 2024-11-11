"""
У нас есть кнопочный телефон (например, знаменитая Nokia 3310), и мы хотим,
чтобы пользователь мог проще отправлять СМС. Реализуем своего собственного клавиатурного помощника.

Каждой цифре телефона соответствует набор букв:
* 2 — a, b, c;
* 3 — d, e, f;
* 4 — g, h, i;
* 5 — j, k, l;
* 6 — m, n, o;
* 7 — p, q, r, s;
* 8 — t, u, v;
* 9 — w, x, y, z.

Пользователь нажимает на клавиши, например 22736368, после чего на экране печатается basement.

Напишите функцию my_t9, которая принимает на вход строку, состоящую из цифр 2–9,
и возвращает список слов английского языка, которые можно получить из этой последовательности цифр.
"""



#22|2777733633668 -> basement
# | для разделения букв если они в одной кнопке идут



from typing import List

old_letters = {
    2 : ['a', 'b', 'c'],
    3 : ['d', 'e', 'f'],
    4 : ['g', 'h', 'i'],
    5 : ['j', 'k', 'l'],
    6 : ['m', 'n', 'o'],
    7 : ['p', 'q', 'r', 's'],
    8 : ['t', 'u', 'v'],
    9 : ['w', 'x', 'y', 'z']
}

#22|2777733633668 -> basement

def my_t9(input_numbers: str) -> List[str]:
    word = []
    help = []
    for num in input_numbers:
        # print(num)
        if not help:
            help.append(num)
            continue
        if num == "|":
            word.append(old_letters[int(help[0])][len(help) - 1])
            help = []
            continue
        if num in help:
            help.append(num)
        else:
            word.append(old_letters[int(help[0])][len(help) - 1])
            help = []
            help.append(num)
    word.append(old_letters[int(help[0])][len(help) - 1])
    return word


if __name__ == '__main__':
    numbers: str = input("Введите строку цифр: ")
    words: List[str] = my_t9(numbers)
    print(''.join(words))
