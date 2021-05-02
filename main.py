# Case-study
# Developers:
# Marinkin O. (38%),
# Seledtsov A. (65%),
# Evdischenko M. (45%)

import turtle,random


def main():
    """
   Funktion that offers to user to choose fractal to see
   :return: None
   """
    num_fr = int(input('''Выберите фрактал, который вы хотите увидеть (укажите цифру):
       1   Квадрат
       2   Двоичное дерево
       3   Фрактал "Ветка"
       4   Кривая Коха
       5   Снежинка Коха
       6   Кривая Минковского
       7   "Ледяной" фрактал. Пример 1
       8   "Ледяной" фрактал. Пример 2
       9   Кривая Леви
       10  Фрактал Дракон Хартера-Хейтуэя
   '''))
    if num_fr == 1:
        square(int(input('Введите сторону квадрата: ')))
    if num_fr == 2:
        turtle.up()
        turtle.goto(0, -200)
        turtle.down()
        turtle.width(4)
        turtle.left(90)
        turtle.speed('fastest')
        n = int(input('Введите глубину рекурсии (рекомендуемая глубина - 6): '))
        size = int(input('Введите длину ветки (рекомендуемая длина - 50): '))
        angle = int(input('Введите угол разветвления дерева (рекомедуется выбрать от 10 до 40): '))
        binary_tree(n, size, angle)
    if num_fr == 3:
        turtle.up()
        turtle.goto(0, -100)
        turtle.down()
        turtle.speed('fastest')
        turtle.left(90)
        n = int(input('Введите глубину рекурсии (рекомендуемая глубина - 6): '))
        size = int(input('Введите длину ветки (рекомендуемая длина - 600): '))
        branch(n, size)
    if num_fr == 4:
        turtle.up()
        turtle.goto(-600, 0)
        turtle.down()
        turtle.pencolor(random_color())
        turtle.speed('fastest')
        order = int(input('Введите глубину рекурсии (рекомендуемая глубина - 5): '))
        size = int(input('Введите длину стороны (рекомендуемая длина - 1200): '))
        koch(order, size)
    if num_fr == 5:
        turtle.up()
        turtle.goto(-300, 150)
        turtle.down()
        turtle.speed('fastest')
        order = int(input('Введите глубину рекурсии (рекомендуемая глубина - 3): '))
        size = int(input('Введите длину стороны (рекомендуемая длина - 600): '))
        kochs_snow(order, size)
    if num_fr == 6:
        turtle.up()
        turtle.goto(-700, -100)
        turtle.down()
        turtle.speed('fastest')
        order = int(input('Введите глубину рекурсии (рекомендуемая глубина - 5): '))
        size = int(input('Введите длину стороны (рекомендуемая длина - 5): '))
        minkovski(order, size)
    if num_fr == 7:
        turtle.up()
        turtle.goto(-800, -100)
        turtle.down()
        turtle.speed('fastest')
        turtle.width(3)
        order = int(input('Введите глубину рекурсии (рекомендуемая глубина - 5): '))
        size = int(input('Введите длину стороны (рекомендуемая длина - 50): '))
        ice_fractal1(order, size)
    if num_fr == 8:
        turtle.up()
        turtle.goto(-350, -100)
        turtle.down()
        turtle.speed('fastest')
        order = int(input('Введите глубину рекурсии (рекомендуемая глубина - 3): '))
        size = int(input('Введите длину стороны (рекомендуемая длина - 50): '))
        ice_fractal2(order, size)
        turtle.left(180)
        ice_fractal2(order, size)
    if num_fr == 9:
        turtle.up()
        turtle.goto(-100, 0)
        turtle.down()
        turtle.speed('fastest')
        order = int(input('Введите глубину рекурсии (рекомендуемая глубина - 8): '))
        size = int(input('Введите длину стороны (рекомендуемая длина - 2400): '))
        levi(order, size)
    if num_fr == 10:
        turtle.up()
        turtle.goto(500, -100)
        turtle.down()
        turtle.speed('fastest')
        turtle.width(3)
        order = int(input('Введите глубину рекурсии (рекомендуемая глубина - 12): '))
        size = int(input('Введите длину стороны (рекомендуемая длина - 8): '))
        harter_haythaways_Dragon(order, size)


def square(a):
    """
   Funktion drawing square in square fractal recursively
   :param a: square side length
   :return: None
   """
    turtle.color(random_color())
    if a < 0:
        return
    for i in range(4):
        turtle.forward(a)
        turtle.left(90)
    turtle.left(10)
    turtle.penup()
    turtle.forward(int(a / 10))
    turtle.pendown()
    square(a - 5)


def binary_tree(n, size, angle):
    """
   Funktion drawing Pifagor's tree fractal recursively
   :param n: recursion depth
   :param size: length of size
   :param angle: tree branch angle
   :return: None
   """
    if n == 0:
        return
    turtle.pencolor('green')
    turtle.forward(size)
    turtle.left(angle)
    binary_tree(n - 1, size, angle)
    turtle.forward(0.33 * size)
    turtle.forward(-0.33 * size)
    turtle.right(2 * angle)
    binary_tree(n - 1, size, angle)
    turtle.forward(0.33 * size)
    turtle.forward(-0.33 * size)
    turtle.left(angle)
    turtle.pencolor('brown')
    turtle.forward(-size)


def koch(order, size):
    """
   Funktion drawing Koch's fractal recursively
   :param order: recursion depth
   :param size: length of size
   :return: None
   """
    if order == 0:
        turtle.forward(size)
    else:
        koch(order - 1, size / 3)
        turtle.left(60)
        koch(order - 1, size / 3)
        turtle.right(120)
        koch(order - 1, size / 3)
        turtle.left(60)
        koch(order - 1, size / 3)


def kochs_snow(order, size):
    """
   Funktion drawing Koch's snow recursively
   :param order: recursion depth
   :param size: length of size
   :return: None
   """
    turtle.color('#b5c3c6')
    turtle.begin_fill()
    koch(order, size)
    turtle.right(120)
    koch(order, size)
    turtle.right(120)
    koch(order, size)
    turtle.end_fill()


def ice_fractal1(order, size):
    """
   Funktion drawing 'ice' fractal recursively
   :param order: recursion depth
   :param size: length of size
   :return: None
   """
    turtle.bgcolor('darkgrey')
    if order == 0:
        turtle.forward(size)
    else:
        turtle.pencolor('indigo')
        ice_fractal1(order - 1, size)
        turtle.left(90)
        ice_fractal1(order - 1, size / 2)
        turtle.left(180)
        ice_fractal1(order - 1, size / 2)
        turtle.left(90)
        ice_fractal1(order - 1, size)


def ice_fractal2(order, size):
    """
   Funktion drawing 'ice' fractal recursively
   :param order: recursion depth
   :param size: length of size
   :return: None
   """
    turtle.bgcolor('lightblue')
    if order == 0:
        turtle.forward(size)
    else:
        turtle.pencolor('seagreen')
        ice_fractal2(order - 1, size)
        turtle.left(120)
        ice_fractal2(order - 1, size / 2)
        turtle.left(180)
        ice_fractal2(order - 1, size / 2)
        turtle.left(120)
        ice_fractal2(order - 1, size / 2)
        turtle.left(180)
        ice_fractal2(order - 1, size / 2)
        turtle.left(120)
        ice_fractal2(order - 1, size)


def levi(order, size):
    """
   Funktion drawing Levi's fractal
   :param order: recursion depth
   :param size: length of size
   :return: None
   """
    turtle.bgcolor('grey')
    if order == 0:
        turtle.forward(size)
    else:
        turtle.pencolor('plum')
        turtle.left(45)
        levi(order - 1, size / 2)
        turtle.right(90)
        levi(order - 1, size / 2)
        turtle.left(45)


def branch(n, size):
    """
   Funktion drawing fractal 'Branch' recursively
   :param n: recursion depth
   :param size: length of size
   :return: None
   """
    turtle.pencolor('goldenrod')
    if n == 0:
        turtle.left(180)
        return

    x = size / (n + 1)
    for i in range(n):
        turtle.forward(x)
        turtle.left(45)
        branch(n - i - 1, 0.5 * x * (n - i - 1))
        turtle.left(90)
        branch(n - i - 1, 0.5 * x * (n - i - 1))
        turtle.right(135)

    turtle.forward(x)
    turtle.left(180)
    turtle.forward(size)


def minkovski(order, size):
    """
   Funktion drawing Minkovski's fractal recursively
   :param order: recursion depth
   :param size: length of size
   :return: None
   """
    turtle.bgcolor('#374d5b')
    if order == 0:
        turtle.forward(size)
    else:
        turtle.pencolor('peru')
        minkovski(order - 1, size)
        turtle.left(90)
        minkovski(order - 1, size)
        turtle.right(90)
        minkovski(order - 1, size)
        turtle.right(90)
        minkovski(order - 1, size)
        minkovski(order - 1, size)
        turtle.left(90)
        minkovski(order - 1, size)
        turtle.left(90)
        minkovski(order - 1, size)
        turtle.right(90)
        minkovski(order - 1, size)


def harter_haythaways_Dragon(order, size):
    """
   Funktion drawing aractal Harter Haythaway's dragon recursively
   :param order: Recursion depth
   :param size: length of size
   :return: None
   """
    if order == 0:
        turtle.forward(size)
    else:
        turtle.pencolor('crimson')
        turtle.begin_fill()
        harter_haythaways_Dragon(order - 1, size)
        turtle.left(90)
        harter_haythaways_Dragon1(order - 1, size)
        turtle.end_fill()


def harter_haythaways_Dragon1(order, size):
    """
   Funktion drawing aractal Harter Haythaway's dragon recursively
   :param order: Recursion depth
   :param size: length of size
   :return: None
   """
    if order == 0:
        turtle.forward(size)
    else:
        turtle.pencolor('darkorange')
        turtle.begin_fill()
        harter_haythaways_Dragon(order - 1, size)
        turtle.right(90)
        harter_haythaways_Dragon1(order - 1, size)
        turtle.begin_fill()


def random_color():
    """Funktion making random color"""
    red = random.random()
    green = random.random()
    blue = random.random()
    return red, green, blue


main()
turtle.mainloop()
