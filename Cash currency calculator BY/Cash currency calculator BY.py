import tkinter as tk

class CurrencyCalculator:
    def __init__(self):
        self.denominations = {
            500: 0,
            200: 0,
            100: 0,
            50: 0,
            20: 0,
            10: 0,
            5: 0,
            2: 0,
            1: 0,
            0.5: 0,
            0.2: 0,
            0.1: 0,
            0.05: 0,
            0.02: 0,
            0.01: 0
        }

        self.total_currency = 0

        self.window = tk.Tk()
        self.window.title("Currency Calculator")
        
        self.label = tk.Label(self.window, text="Введите количество банкнот каждого номинала:")
        self.label.pack()

        # Создаем поля ввода для каждого номинала
        self.entries = {}
        for value in self.denominations:
            input_frame = tk.Frame(self.window)
            input_frame.pack()
            label = tk.Label(input_frame, text=f"Номинал {value}:")
            label.pack(side=tk.LEFT)
            entry = tk.Entry(input_frame)
            entry.pack(side=tk.LEFT)
            self.entries[value] = entry

        self.calculate_button = tk.Button(self.window, text="Посчитать", command=self.calculate_total)
        self.calculate_button.pack()

        self.total_label = tk.Label(self.window, text="")
        self.total_label.pack()

        self.window.mainloop()

    def calculate_total(self):
        self.total_currency = 0

        # Получаем количество банкнот для каждого номинала из полей ввода
        for value, entry in self.entries.items():
            try:
                quantity = int(entry.get())
                self.denominations[value] = quantity
                self.total_currency += value * quantity
            except ValueError:
                pass

        self.total_label.config(text=f"Общая наличность: {self.total_currency} рублей")

# Создаем экземпляр класса CurrencyCalculator
calculator = CurrencyCalculator()
