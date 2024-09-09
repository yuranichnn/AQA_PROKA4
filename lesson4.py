# Задание №1
numbers = [1, 2, 3, 4, 5]
print(numbers[2])
numbers.append(10)
del numbers[1]
print(numbers)

# Задание №2
fruits = ["apple", "orange", "banana"]
combined = numbers + fruits
print(len(combined))
print(combined[-1])
combined_slice = combined[1:4]

# Задание №3
combined_copy = combined[:]
combined_copy[0] = "яблоко"
print(combined)
print(combined_copy)