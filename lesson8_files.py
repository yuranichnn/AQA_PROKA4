# Задание №1
with open("data.txt", "w+") as file:
    file.write('''Hello world!
           Its good day today
           Have a nice day, man''')
    file.seek(0)
    content_file = file.readlines()

for element in content_file:
    line = element.strip()
    print(line)

# Задание №2
name = input("Введите ваше имя:")
age = input("Введите ваш возвраст:")
with open("userinfo.txt", "a+") as file:
    file.write(f"{name}:{age}\n")

# Задание №3
with open("original.txt", "w+") as original_file:
    original_file.write("Это содержимое файла original.txt.\nТестирование копирования файлов.")
    original_file.seek(0)
    context_original_file = original_file.read()
with open("copy.txt", "w") as copy_file:
    copy_file.write(context_original_file)
