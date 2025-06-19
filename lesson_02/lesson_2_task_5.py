n = int(input("Введите номер месяца: "))


def month_to_season(n):
    if (n <= 2 or n == 12) and n != 0:
        print("Зима")
    elif n >= 3 and n <= 5:
        print("Весна")
    elif n >= 6 and n <= 8:
        print("Лето")
    elif n >= 9 and n <= 11:
        print("Осень")
    else:
        print("Неверный номер месяца")


month_to_season(n)
