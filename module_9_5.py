class StepValueError(ValueError):
    pass


class Iterator:

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.pointer = self.start
        if step != 0:
            self.step = step
        else:
            raise StepValueError('Шаг не может быть равен 0')

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        current = self.pointer
        if self.step > 0 and current <= self.stop or self.step < 0 and current >= self.stop:
            self.pointer += self.step
            return current
        else:
            raise StopIteration()


# Проверка кода
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()

for i in iter3:
    print(i, end=' ')
print()

for i in iter4:
    print(i, end=' ')
print()

for i in iter5:
    print(i, end=' ')
print()


# Старая версия задачи
print('Прежняя версия задачи')

class EvenNumbers:

    def __init__(self, start=0, end=1):
        self.start = start
        if self.start < end:
            self.end = end
        else:
            print('Атрибут end не может быть меньше или равным атрибуту start.')

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            if self.start % 2 == 0:
                result = self.start
            else:
                result = self.start + 1
            self.start += 2
            return result
        else:
            raise StopIteration()


# Проверка кода:
en = EvenNumbers(10, 25)

for i in en:
    print(i)
