# Задача 'Функциональное разнообразие'.


# Lambda-функция.
first = 'Мама мыла раму'
second = 'Рамена мало было'

lambda_function = list(map(lambda x, y: True if x == y else False, first, second))
print(lambda_function)


# Замыкание.
def get_advanced_writer(file_name):
    ''' :param file_name - название файла для записи '''

    def write_everything(*data_set):
        ''' :param data_set - неограниченное количество данных любого типа '''
        with open(file_name, 'a+', encoding='utf-8') as f:
            for string in data_set:
                f.write(str(string) + '\n')

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'], 'И здесь могут быть еще данные')


# Метод '__call__'.
from random import choice


class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Возможно', 'Конечно')
print(first_ball())
print(first_ball())
print(first_ball())
