# gui.py
import tkinter as tk
import functions

# Создаем словарь с функциями и их документацией
function_documentation = {
    "add": functions.add.__doc__,
    "subtract": functions.subtract.__doc__,
    "multiply": functions.multiply.__doc__,
    "divide": functions.divide.__doc__,
    "power": functions.power.__doc__,
}


def show_documentation(function_name):
    """
    Выводит документацию для выбранной функции.

    Параметры:
    - function_name (str): Имя функции.
    """
    docstring = function_documentation[function_name]
    documentation_label.config(text=docstring)


def create_gui():
    """
    Создает графический интерфейс с кнопками для вызова функций и вывода документации.
    """
    window = tk.Tk()
    window.title("Модуль работы с целыми числами")
    window.configure(background="white")

    function_names = ["add", "subtract", "multiply", "divide", "power"]

    for function_name in function_names:
        # Создаем кнопку для каждой функции и привязываем к ней функцию вывода документации
        button = tk.Button(
            window,
            text=function_name.capitalize(),
            command=lambda fn=function_name: show_documentation(fn),
            relief=tk.FLAT,
            background="#ADD8E6",  # Light Blue
            foreground="#00008B",  # Dark Blue
            padx=10,
            pady=5
        )
        button.pack(pady=5)

    # Добавляем метку для отображения документации
    global documentation_label
    documentation_label = tk.Label(window, text="Документация будет отображена здесь.")
    documentation_label.pack()

    window.mainloop()


if __name__ == "__main__":
    create_gui()
