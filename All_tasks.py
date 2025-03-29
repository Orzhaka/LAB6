from datetime import datetime

def task1():
    def na3(a):
        if a%3 == 0:
            print(f"{num} делится на 3")
        else:
            print(f"{num} не делится на 3")

    num = int(input("Введите число для проверки: "))
    na3(num)


def task2():
    try:
        num = int(input("Введите число: "))
        res = 100 / num
        print(f"100 / {num} = {res}")
    except ValueError:
        print("Ошибка: Введите корректное число.")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль невозможно.")


def task3():
    def is_magic_date(date_str):
        date = datetime.strptime(date_str, "%d.%m.%Y")
        if date.day * date.month == int(str(date.year)[-2:]):
            return "Магическая дата"
        else:
            return "Не магическая дата"

    user_date = input("Введите дату (дд.мм.гггг): ")
    print(is_magic_date(user_date))


def task4():
    def happy(num):
        if len(num) != 6 or not num.isdigit():
            print("Ошибка: номер билета должен содержать ровно 6 цифр.")

        first_half = 0
        second_half = 0

        for i in range(3):
            first_half += int(num[i])
            second_half += int(num[i + 3])

        if first_half == second_half:
            print("Ваш билет счастливый")
        else:
            print("Обычный билет")

    s = input("Введите номер счастливого билета: ")
    happy(s)


choice = int(input("Введите номер задания без пробелов (от 1 до 4): "))

if choice == 1:
    task1()
elif choice == 2:
    task2()
elif choice == 3:
    task3()
elif choice == 4:
    task4()
else:
    print("Ошибка: введите корректный номер задания")