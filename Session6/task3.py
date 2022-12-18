# Задача 3. Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

number = int(input("Введите число: "))
lst = []

for i in range(number): # Первый вариант
    lst.append((-3)**i)
print(f"Итоговая последовательность: {lst}")

# Второй вариант, для правильной работы перенести на строку 8

# lst = [(-3)**i for i in range(number)]
# print(f"Последовательность применения list comprehension: {lst}")