from random import randint as rnd
import math

# Напишите программу, чтобы найти значение указанного выражения.
from typing import Dict, List


def expressions() -> list[int]:
    a = (101 + 0) / 3
    b = 3 * math.e * 10000000.1
    c = True and True
    d = False and True
    e = (False and False) or (True and True)
    f = (False or False) and (True and True)
    return [a, b, c, d, e, f]


# Напишите программу, которая принимает четыре целых числа от
# пользователя и выводит надпись равно, если все четыре равны,
# и не равно в противном случае.
def comparison() -> str:
    print("введите 4 цифры, чтобы мы их сравнили")
    a = int(input())
    output = "Равно"
    for i in range(3):
        b = int(input())
        if a != b:
            output = "Не равно"
    return output


# for 3-7 ex
def array_generator(_len: int = 50, _min: int = 0, _max: int = 100) -> list[int]:
    new_list = [rnd(_min, _max) for i in range(_len)]
    return new_list


#  Напишите программу для поиска k самых больших элементов
#  в заданном массиве. Элементы в массиве могут
#  располагаться в любом порядке.
def search_max_numbers(array: list[int], count: int = 3) -> list[int]:
    max_numbers = []
    for i in range(count):
        maximum = max(array)
        array.pop(array.index(maximum))
        max_numbers.append(maximum)

    return max_numbers


# Напишите программу для поиска k наименьших элементов
# в заданном массиве. Элементы в массиве могут
# располагаться в любом порядке.
def search_min_numbers(array: list[int], count: int = 3) -> list[int]:
    min_numbers = []
    for i in range(count):
        minimum = min(array)
        array.pop(array.index(minimum))
        min_numbers.append(minimum)

    return min_numbers


# 5. Напишите программу для поиска чисел,
# превышающих среднее значение чисел данного массива.
def more_then_avarage(array: list[int]) -> list[int]:
    avarage = sum(array) / len(array)
    output = []
    for i in array:
        if i > avarage:
            output.append(i)
    return output


# 6. Напишите программу для умножения
# двух заданных целых чисел без
# использования оператора умножения(*).
def mul_two_num(a, b) -> int:
    mul_output = 0
    for i in range(a):
        mul_output += b
    return mul_output


# 7. Напишите для разбиения заданного
# массива целых чисел на четное число первым
# и нечетное число вторым.
def even_odd_arrays(array: list[int]) -> dict[str, list[int]]:
    odd_array = []
    even_array = []
    for i in array:
        if i % 2 == 0:
            even_array.append(i)
        else:
            odd_array.append(i)

    return {"even": even_array, "odd": odd_array}


# 8. Напишите програмиу для преобразования
# температуры из градуса Фаренгейта в градус Цельсия.
def fahrenheit_celsius(gradus: float) -> float:
    new_gradus = (gradus - 32) * 5 / 9
    return new_gradus


# 9. Напишите программу для вычисления индекса
# массы тела (ИМТ). ИМТ = ВЕС / РОСТ2
def index_weight(weight: float, height: float) -> float:
    imt = weight / (height * 2)
    return imt


# 10. Напишите, которая считывает число и
# отображает квадрат, куб и четвертую степень.
def power_number(number: int) -> dict[str, int]:
    power_2th = number ** 2
    power_3th = number ** 3
    power_4th = number ** 4
    return {"2h": power_2th, "3th": power_3th, "4th": power_4th}


# 11. Напишите программу, чтобы проверить,
# могут ли три заданные длины сторон (целые числа)
# образовать треугольник или нет.
def triangle_input():
    first = int(input("Введите длинну первой стороны: "))
    second = int(input("Введите длинну второй стороны: "))
    thrith = int(input("Введите длинну третей стороны: "))

    if first + second <= thrith or second + thrith <= first or first + thrith <= second:
        print("Не существует")
        return None
    print("Существо")
    return [first, second, thrith]


def main():
    print(expressions())
    print(comparison())

    array = array_generator()
    print(f"Array = {array}")
    count = int(input("Сколько цифр надо искaть? "))
    print(f"Max = {search_max_numbers(array, count)}")
    print(f"Min = {search_min_numbers(array, count)}")
    print(f"More then avarage = {more_then_avarage(array)}")

    a = int(input('Введите 2 цифры для умножения\n'))
    b = int(input())
    print(f"Значение умножения: {mul_two_num(a, b)}")
    print(even_odd_arrays(array))

    gradus_fahrenheit = float(input("Введите градус форенгейта: "))
    print(f"celsius = {fahrenheit_celsius(gradus_fahrenheit)}")

    weight = float(input("Вес: "))
    height = float(input("Рост: "))
    print(index_weight(weight, height))

    number = int(input(("Введите число: ")))
    print(power_number(number))

    triangle = triangle_input()
    print(triangle)

if __name__ == "__main__":
    main()
