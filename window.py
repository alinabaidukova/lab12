import tkinter as tk

class window:   #класс для графического окна
    def __init__(self, flavors):
        self.flavors = flavors
        self.window = tk.Tk()   #активация конструктора
        self.label_title = tk.Label(self.window, text="Вкусы мороженого:")  #заголовок
        self.label_title.pack() #добавление заголовка в окно
        self.listbox_flavors = tk.Listbox(self.window)  #для отображения вкусов
        self.listbox_flavors.pack() #добавление вкусов в окно

        for flavor in self.flavors: #добавление каждого вкуса по очереди
            self.listbox_flavors.insert(tk.END, flavor)

    def run(self):  #запуск и появление окна
        self.window.mainloop()

class IceCreamStand:
    def __init__(self, flavors):
            self.flavors = flavors

    def print(self):  #метод для вывода вкусов
        print("Вкусы мороженого:")
        for flavor in self.flavors:
            print(flavor)

flavors = ["Шоколад", "Ваниль", "Клубника", "Карамель"]

iceCreamStand = IceCreamStand(flavors)  #для вывода вкусов
iceCreamStand.print()

show = window(flavors)
show.run()
