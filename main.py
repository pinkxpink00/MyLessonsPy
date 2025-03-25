# CONST_NAME = "Привет это небольшая программа для теста"
# print(CONST_NAME)
#
# userName = input("input ur name: ")
# welcomeMessage = f"Hello {userName}"
# print (welcomeMessage)
import sys

try:
    userVar = int(input("Введите число: "))

    if userVar <= 55:
        print(True)
        print("End")
    elif userVar <= 100:
        print("Digits <= 100")


except ValueError:
    print("Ошибка: введено не число!", file=sys.stderr)
