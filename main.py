# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
num = 5
print(num)
name = "Garegin"
bool_eat = True
print(name)
name1 = input("Введите Ваше имя ")
print(f"Привет {name1}")
#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
time_seconds = int(input("Введите секунды "))
time_hour = time_seconds // 3600
time_minutes = (time_seconds // 60) - (time_hour * 60)
time_seconds1 = time_seconds - (time_hour * 60 + time_minutes) * 60
print(f"{time_hour} часа : {time_minutes}  минут : {time_seconds1} секунд")
#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
numbers = int(input("Введите число "))
numbers_string = str(numbers) + str(numbers)
numbers_string1 = str(numbers) + str(numbers) + str(numbers)
numbers_sum = numbers + int(numbers_string) + int(numbers_string1)
print(numbers_sum)
#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
numbers_users = int(input("Введите целое число "))