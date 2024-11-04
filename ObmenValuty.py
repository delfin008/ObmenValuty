from tkinter import *
from tkinter import messagebox as mb

import requests
from tkinter import ttk


def update_b_label(event):
    code = b_combobox.get()
    name = curs[code]
    b_label.config(text=name)

def update_t_label(event):
    code = t_combobox.get()
    name = curs[code]
    t_label.config(text=name)


def exchange():
    t_code = t_combobox.get()
    b_code = b_combobox.get()
    b2_code = b2_combobox.get()

    if t_code and b_code and b2_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{b_code}')
            response.raise_for_status()
            data = response.json()
            if t_code in data['rates']:
                exchange_rate = data['rates'][t_code]
                t_name = curs[t_code]
                b_name = curs[b_code]
                b2_name = curs[b2_code]
                mb.showinfo("Курс обмена базовой валюты", f"Курс: {exchange_rate:.2f} {t_name} за 1 {b_name},")
                mb.showinfo("Курс обмена второй базовой валюты", f"Курс: {exchange_rate:.2f} {t_name} за 1 {b2_name},")
            else:
                mb.showerror("Ошибка!", f"Валюта {t_code} не найдена!")
                mb.showerror("Ошибка!", f"Валюта {b_code} не найдена!")
                mb.showerror("Ошибка!", f"Валюта {b2_code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}")
    else:
        mb.showwarning("Внимание!", f"Введите код валюты!")

curs = {
    'RUB': 'Руссийский рубль',
    'EUR': 'Евро',
    'GBP': 'Британский фунт стерлингов ',
    'JPY': 'Японская йена',
    'CNY': 'Китайский юань',
    'KZT': 'Казахский тенге',
    'UZS': 'Узбекский сум',
    'CHF': 'Швейцарский франк',
    'AED': 'Дирхам ОАЭ',
    'CAD': 'Канадский доллар',
    'USD': 'Американский доллар'}


window = Tk()
window.title("Курс обмена валют")
window.geometry("360x400")

Label(text="Базовая валюта").pack(padx=10, pady=10)

b_combobox = ttk.Combobox(values=list(curs.keys()))
b_combobox.pack(padx=10, pady=10)
b_combobox.bind("<<ComboboxSelected>>", update_b_label)

b_label = ttk.Label()
b_label.pack(padx=10, pady=10)

Label(text="Вторая базовая валюта").pack(padx=10, pady=10)

b2_combobox = ttk.Combobox(values=list(curs.keys()))
b2_combobox.pack(padx=10, pady=10)





Label(text="Целевая валюта").pack(padx=10, pady=10)

t_combobox = ttk.Combobox(values=list(curs.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)

t_label = ttk.Label()
t_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена валют", command=exchange).pack(padx=10, pady=10)

window.mainloop()