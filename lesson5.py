# Задание №1
num = int(input("Введите целое число - "))
if num > 0:
    if 0 < num < 10:
        print("Число от 1 до 9")
    elif num >= 10:
        print("Число 10 и больше")
    else:
        print("Число положительное")
elif num == 0:
    print("Число равно нулю")
else:
    print("Число отрицательное")

# Задание №2
is_raining = True
is_sunny = False
if is_raining and is_sunny:
    print("Дождь при солнце, возможна радуга!")
elif not is_raining and is_sunny:
    print("Сегодня солнечная погода, отличный день для прогулки!")
elif is_raining and not is_sunny:
    print("Сегодня идет дождь, возьмите зонт!")
else:
    print("Сегодня облачно, но без осадков")
