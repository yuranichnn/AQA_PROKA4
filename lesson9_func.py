# Задание №1
def summa(*args):
    summ = 0
    for number in args:
        summ += number
    return summ


def max_in_list(numbers: list):
    max_number = max(numbers)
    return max_number


def say_hello(name):
    print(f"Hello {name}")


# Задание №2
def buy_tickets(full_name, age, adult=False):
    if age >= 18:
        print(f"{full_name} - вам продан билет")
    elif age < 18 and adult:
        print(f"{full_name} - вам продан билет под присмотром взрослого")
    else:
        print(f"{full_name} - вам нельзя продать билет")


# Задание №3
def square_numbers_in_list(numbers: list):
    return [number**2 for number in numbers]


