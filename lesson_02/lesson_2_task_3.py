import math

input_side = float(input("Введите значение стороны:"))
input_side = math.ceil(input_side)


def square(side):
    sq = side*side
    return sq


result = square(input_side)
print("Площадь равна:" + str(result))
