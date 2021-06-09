import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

class CurrencyConverter():
    # create contructor
    def __init__(self, url):
        # getting data from api , format json
        self.data = requests.get(url).json()
        # print(self.data)
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        init_amount = amount

        # ubah input data from user if USD to USD
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]

        # buat hasil menjadi 4 angka dibelakang koma
        amount = round(amount * self.currencies[to_currency], 4)

        return amount


# running program
url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = CurrencyConverter(url)
print(converter.convert('INR', 'USD', 15000))


# create UI Currency Converter
class UI():
    # create constructor
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title = 'Pengubah Mata Uang'
        self.converter = converter