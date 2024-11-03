import requests
import json
from tkinter import *
from tkinter import messagebox as mb


from PyInstaller.loader.pyiboot01_bootstrap import entry
from gevent.testing.travis import command

window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x180")

Label(text="Введите код валюты").pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Batton(text="Получить курс обмена кдоллару", command=extended).pack(padx=10, pady=10)

window,mainloop()