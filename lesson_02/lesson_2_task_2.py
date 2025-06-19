
year = int(input("Введите год:"))


def is_year_leap(year_loc):
    res = year_loc % 4
    if res == 0:
        return "True"
    else:
        return "False"


result = is_year_leap(year)
print("год " + str(year) + ": " + result)
