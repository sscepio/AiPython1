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
numbers_users = str(input("Введите целое число "))
count_numbers = int(numbers_users[0])
i = 0
while i < len(numbers_users):

    if count_numbers <= int(numbers_users[i]):
        count_numbers = int(numbers_users[i])
    i = i + 1
print(count_numbers)
#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника
P = int(input("Введите выручку "))
C = int(input("Введите издержки "))
if P - C > 0:
    print("Компания прибыльна")
    print(f"Рентабельность составляет {P // C * 100}%")
else:
    print("Компания убыточна")
E = int(input("Введите количество сотрудников "))
print(f"Рентабельность на одного сотрудника составляет {(P - C) // E} рублей")
#6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
A = int(input("Введите значение a "))
B = int(input("Введите значение b "))
i_day = 1
while A < B:
    print(f"На {i_day}-й день результат {A:.2f} км")
    i_day = i_day + 1
    A = A + A * 0.1
print(f"На {i_day}-й день результат {A:.2f} км")
print(f"На {i_day}-й день спортсмен достиг результата — не менее {B} км.")

