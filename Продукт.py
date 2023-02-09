import matplotlib.pyplot as pl
import numpy as nup

def plot_function(ax, func, value):
    X = nup.linspace(-nup.pi, nup.pi, 256)
    Y = nup.linspace(-nup.pi, nup.pi, 256)
    X, Y = nup.meshgrid(X, Y)
    Z = func(value * nup.sqrt(X**2 + Y**2))

    ax.plot_surface(X, Y, Z, cmap='plasma')
    ax.set_title("Функция")import matplotlib.pyplot as pl
import numpy as nup

def plot_function_2d(ax, func, value):
    X = nup.linspace(-nup.pi, nup.pi, 256)
    Y = funct(value * X)

    ax.plot(X, Y)
    ax.set_title("Функция")
    ax.set_xlabel("X координата")
    ax.set_ylabel("Y координата")

def plot_function_3d(ax, func, value):
    X = nup.linspace(-nup.pi, nup.pi, 256)
    Y = nup.linspace(-nup.pi, nup.pi, 256)
    X, Y = nup.meshgrid(X, Y)
    Z = func(value * nup.sqrt(X**2 + Y**2))

    ax.plot_surface(X, Y, Z, cmap='plasma')
    ax.set_title("Функция")
    ax.set_xlabel("X координата")
    ax.set_ylabel("Y координата")
    ax.set_zlabel("Z координата")

def funct_x(value):
    return value

def funct_x_squared(value):
    return value ** 2

def funct_sqrt(value):
    return nup.sqrt(value)

if __name__ == '__main__':
    fig = pl.figure()
    ax = fig.add_subplot(111, projection='3d')

    functions = {
        'sin': nup.sin,
        'cos': nup.cos,
        'tan': nup.tan,
        'exp': nup.exp,
        'log': nup.log,
        'x': funct_x,
        'x^2': funct_x_squared,
        'sqrt(x)': funct_sqrt
    }

    choice = input("Выберете функцию из списка 'sin', 'cos', 'tan', 'exp', 'log', 'x', 'x^2', 'sqrt(x)': ")
    funct = functions.get(choice)
    if funct is None:
        print("Неверный выбор")
        exit()

    value = float(input("Введите значение функции: "))

    if choice in ['x', 'x^2', 'sqrt(x)']:
        fig = pl.figure()
        ax = fig.add_subplot(111)
        plot_function_2d(ax, funct, value)
    else:
        fig = pl.figure()
        ax = fig.add_subplot(111, project='3d')
        plot_function_3d(ax, funct, value)

    pl.tight_layout()
    pl.show()

    ax.set_xlabel("X координата")
    ax.set_ylabel("Y координата")
    ax.set_zlabel("Z координата")

if __name__ == '__main__':
    fig = pl.figure()
    ax = fig.add_subplot(111, projection='3d')

    functions = {
        'sin': nup.sin,
        'cos': nup.cos,
        'tan': nup.tan,
        'exp': nup.exp,
        'log': nup.log
    }

    choice = input("Выберете функцию из списка 'sin', 'cos', 'tan', 'exp', 'log': ")
    funct = functions.get(choice)
    if funct is None:
        print("Неверный выбор")
        exit()

    value = float(input("Введите значение функции: "))
    plot_function(ax, funct, value)

    pl.tight_layout()
    pl.show()
