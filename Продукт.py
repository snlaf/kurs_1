import matplotlib.pyplot as pl
import numpy as nup

def plot_function(ax, func, value):
    X = nup.linspace(-nup.pi, nup.pi, 256)
    Y = nup.linspace(-nup.pi, nup.pi, 256)
    X, Y = nup.meshgrid(X, Y)
    Z = func(value * nup.sqrt(X**2 + Y**2))

    ax.plot_surface(X, Y, Z, cmap='plasma')
    ax.set_title("Функция")
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
