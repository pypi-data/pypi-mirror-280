import math
def number31():
   #Найти модуль комплексного числа z = -2+2i√3
    # Действительная и мнимая части комплексного числа
    a = -2
    b = 2 * math.sqrt(3)

    # Вычисление модуля комплексного числа
    r = math.sqrt(a**2 + b**2)

    # Округление результата до ближайшего целого числа
    rounded_r = round(r)

    # Вывод результата
    print(f"Модуль комплексного числа z = -2 + 2i√3 равен {rounded_r}")

def number32():
    #Найти произведение чисел z1= 3(cos 270°+i sin 270°) и z2=√2(cos 45°+i sin 45°).
    # Ответ записать в алгебраической форме.
    # Дано
    r1 = 3
    theta1 = 270
    r2 = math.sqrt(2)
    theta2 = 45

    # Переводим углы в радианы
    theta1_rad = math.radians(theta1)
    theta2_rad = math.radians(theta2)

    # Вычисляем произведение модулей
    r = r1 * r2

    # Вычисляем сумму аргументов
    theta = theta1_rad + theta2_rad

    # Переводим результат в алгебраическую форму
    real_part = r * math.cos(theta)
    imaginary_part = r * math.sin(theta)

    # Округляем действительную и мнимую части до ближайшего целого числа
    rounded_real_part = round(real_part)
    rounded_imaginary_part = round(imaginary_part)

    # Выводим ответ
    print(f"Ответ: z = {rounded_real_part}{rounded_imaginary_part}i")

def number33():
    #Найти частное чисел z1= 54(cos 210°+i sin 210°) и z2=2(cos 30°+i sin 30°).
    # Ответ записать в алгебраической форме.
    # Дано
    r1 = 54
    theta1 = 210
    r2 = 2
    theta2 = 30

    # Переводим углы в радианы
    theta1_rad = math.radians(theta1)
    theta2_rad = math.radians(theta2)

    # Вычисляем частное модулей
    r = r1 / r2

    # Вычисляем разность аргументов
    theta = theta1_rad - theta2_rad

    # Переводим результат в алгебраическую форму
    real_part = r * math.cos(theta)
    imaginary_part = r * math.sin(theta)

    # Выводим ответ
    print(f"Ответ: z = {int(real_part)}")