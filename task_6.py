"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word):
    try:
        return word.title()
    except AttributeError:
        print("Необходимо ввести буквенное выражение!")


print(int_func("humor"))
print(int_func(input("Введите слово из маленьких латинских букв: ")))


def int_func_1(words):
    my_list = words.split()
    for ind, word in enumerate(my_list):
        my_list[ind] = int_func(word)
    return ' '.join(my_list)


print(int_func_1("sens of humor"))
print(int_func_1(input("Введите слово из маленьких латинских букв: ")))
