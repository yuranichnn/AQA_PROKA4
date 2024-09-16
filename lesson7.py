# Задание №1
numbers_list = list()
for element in range(0, 101):
    numbers_list.append(element)

# Задание №2
while len(numbers_list) != 51:
    del numbers_list[-1]

print(numbers_list)

# Задание №3
begin = 1
end = 100
number = begin
divisor = 7

while number <= end:
    if number % divisor == 0 and number != 0:
        print(f"Первое число, делящееся на {divisor} без остатка в диапазоне от {begin} до {end}: {number}")
        break
    number += 1

# Альтернативное решение
first_multiple = (begin + divisor - 1) // divisor * divisor
print(f"Первое число, делящееся на {divisor} без остатка в диапазоне от {begin} до {end}: {first_multiple}")
