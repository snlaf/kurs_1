import matplotlib.pyplot as pl
import numpy as nup


def plot_function_2d(func, value):
    fig, ax = pl.subplots()
    X = nup.linspace(-nup.pi, nup.pi, 256)
    Y = func(value * X)
    ax.plot(X, Y)

    ax.set_title("Функция")
    ax.set_xlabel("X координата")
    ax.set_ylabel("Y координата")
    pl.show()


def plot_function_3d(func, value):
    fig = pl.figure()
    ax = fig.add_subplot(111, projection='3d')
    X = nup.linspace(-nup.pi, nup.pi, 256)
    Y = nup.linspace(-nup.pi, nup.pi, 256)
    X, Y = nup.meshgrid(X, Y)
    Z = func(value * nup.sqrt(X ** 2 + Y ** 2))

    ax.plot_surface(X, Y, Z, cmap='plasma')
    ax.set_title("Функция")
    ax.set_xlabel("X координата")
    ax.set_ylabel("Y координата")
    ax.set_zlabel("Z координата")
    pl.show()


def funct_x(value):
    return value


def funct_x_squared(value):
    return value ** 2


def funct_sqrt(value):
    return nup.sqrt(value)


def funct_ctg(value):
    return 1 / nup.tan(value)


if __name__ == '__main__':
    functions = {
        'sin': nup.sin,
        'cos': nup.cos,
        'tan': nup.tan,
        'ctg': funct_ctg,
        'exp': nup.exp,
        'log': nup.log,
        'x': funct_x,
        'x^2': funct_x_squared,
        'sqrt(x)': funct_sqrt
    }

    while True:
        choice = input(
            "Выберете функцию из списка 'sin', 'cos', 'tan', 'ctg', 'exp', 'log', 'x', 'x^2', 'sqrt(x)' или введите 'exit' для выхода: ")
        if choice == 'exit':
            break
        else:
            funct = functions.get(choice)
            value = float(input("Введите значение функции: "))
            dim = input("Выберете кол-во измерений (2 или 3): ")
            if dim == '2':
                plot_function_2d(funct, value)
            elif dim == '3':
                plot_function_3d(funct, value)
            else:
                print("Неверный выбор")
                exit()