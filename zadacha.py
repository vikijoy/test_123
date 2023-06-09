#1. Реализуйте 3 метода, чтобы в каждом из них получить разные исключения

a, b = int(input()), int(input()) #принимаем два числа и проверяем на неделимость на ноль
try:
    print(a / b)
except ZeroDivisionError:
    print('Нельзя делить на ноль')

x, y = input().split() #проверяем, являются ли вводимые значения числами
try:
    print(isinstance(x, int) and isinstance(y, int))
except TypeError:
    print('Number mus be an integer')

cities = input().split() #принимаем список городов, проверяем есть ли в списке не str
if all(map(lambda x: x.isalpha(), cities)):
    print('Alrighht')
else:
    raise ValueError('No numbers in the list of the ciities allowed')

#2. Реализуйте метод, принимающий в качестве аргументов два целочисленных массива,
# и возвращающий новый массив, каждый элемент которого равен разности элементов
# двух входящих массивов в той же ячейке. Если длины массивов не равны, необходимо
# как-то оповестить пользователя.

class HometaskError(Exception):
    '''Мой пользовательский класс, не писал методы класса, лишь унаследовал от родительского класса
    так как требуется лишь оповестить юзера об ошибке'''
    pass


def check_array(arr: list, lst: list) -> list:
    if len(arr) != len(lst):
        raise HometaskError('Длины списков неравны!')
    else:
        return list(map(sum, zip(arr, lst)))

#3. * Реализуйте метод, принимающий в качестве аргументов два целочисленных массива,
# и возвращающий новый массив, каждый элемент которого равен частному элементов двух
# входящих массивов в той же ячейке. Если длины массивов не равны, необходимо как-то
# оповестить пользователя. Важно: При выполнении метода единственное исключение, которое
#  пользователь может увидеть - RuntimeException, т.е. ваше.

def check_array_second(arr: list, lst: list) -> list:
    if len(arr) != len(lst):
        raise HometaskError('Длины списков неравны!')
    else:
        return list(map(lambda x: x[0] / x[1], zip(arr, lst)))