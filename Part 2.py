class ZeroDivisionError(Exception):
    def __init__(self):
        print("На ноль делить нельзя!")

try:
    a=int(input("Введите делимое - "))
    b=int(input("Введите делитель - "))
    if b==0:
        raise ZeroDivisionError
    else: print(a/b)
except ZeroDivisionError:
    pass

