import tkinter as tk
import requests


window = tk.Tk()
window.geometry("500x300")
window.title("Currency Convetor")
window.config(bg="#202630")

def convert_currency():
    amount = float(entry_amount.get())
    from_currency = currency_from.get()
    to_currency = currency_to.get()


    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(api_url)
    data = response.json()
    exchange_rate = data["rates"][to_currency]
    converted_amount = amount * exchange_rate

    result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

head_lable = tk.Label(window,text="Currency Converter",font="Times 20 bold",bg="#202630",fg="purple")
head_lable.pack()
amount_label = tk.Label(window,text="Amount",font="Times 20 bold",bg="#202630",fg="purple")
amount_label.pack()
entry_amount = tk.Entry(window)
entry_amount.pack()

currency_from = tk.StringVar()
currency_to = tk.StringVar()

currency_from.set("INR")
currency_to.set("USD")

currency_from_label = tk.Label(window, text="From Currency:",font="Times 20 bold",bg="#202630",fg="purple")
currency_from_menu = tk.OptionMenu(window, currency_from, "INR", "EUR", "GBP","USD","CNY","EUR","CAD","DKK","GBP")
currency_from_menu.config(font="Times 10 ",bg="gray",fg="black")
currency_from_label.pack()
currency_from_menu.pack()

currency_to_label = tk.Label(window, text="To Currency:",font="Times 20 bold",bg="#202630",fg="purple")
currency_to_menu = tk.OptionMenu(window, currency_to, "INR", "EUR", "GBP","USD","CNY","EUR","CAD","DKK","GBP")
currency_to_menu.config(font="Times 10 ",bg="gray",fg="black")
currency_to_label.pack()
currency_to_menu.pack()

convert_button = tk.Button(window, text="Convert", command=convert_currency,font="Times 10 ",bg="gray",fg="black")
convert_button.pack()

result_label = tk.Label(window, text="",bg="#202630",fg="purple",font="Times 15 bold")
result_label.pack()

window.mainloop()
