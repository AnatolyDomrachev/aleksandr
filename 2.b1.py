# Begin 1
'''
Дана сторона квадрата a. Найти его периметр P = 4·a.
'''

while True: # Цикл
    a = input("введите а: ")

    if a.isdigit(): # Условие
        a = int(a)
        break
    else:
            print("Вы ввели не число, повторите ввод")

p = 4*a
print("Периметр = ", p);
