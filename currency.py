import tkinter as tk
from tkinter import ttk
from currency_converter import CurrencyConverter

c = CurrencyConverter()

class CurrencyConverterApp:
    def __init__(self, controller):
        self.controller = controller
        self.controller.title("Currency Converter")

        # Adding theme
        self.style = ttk.Style()
        self.style.theme_use("clam")

        # Adding icon for the app
        self.controller.wm_iconbitmap('file.ico')  

        mainframe = ttk.Frame(controller, padding="10 15 60 5")
        mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Amount label and entry
        self.amount_label = ttk.Label(mainframe, text="Amount:")
        self.amount_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        
        self.amount_entry = ttk.Entry(mainframe, width=20)
        self.amount_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

        # From currency label and dropdown
        self.from_currency_label = ttk.Label(mainframe, text="From:")
        self.from_currency_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

        self.from_currency = tk.StringVar()
        self.from_currency_combobox = ttk.Combobox(mainframe, textvariable=self.from_currency)
        self.from_currency_combobox['values'] = ('USD','JPY','BGN','CYP','CZK','DKK','EEK','GBP','HUF','LTL','LVL','MTL','PLN','ROL','RON','SEK','SIT','SKK','CHF','ISK','NOK','HRK','RUB','TRL','TRY','AUD','BRL','CAD','CNY','HKD','IDR','ILS','INR','KRW','MXN','MYR','NZD','PHP','SGD','THB','ZAR')
        self.from_currency_combobox.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
        self.from_currency_combobox.current(0)

        # To currency label and dropdown
        self.to_currency_label = ttk.Label(mainframe, text="To:")
        self.to_currency_label.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

        self.to_currency = tk.StringVar()
        self.to_currency_combobox = ttk.Combobox(mainframe, textvariable=self.to_currency)
        self.to_currency_combobox['values'] = ('USD','JPY','BGN','CYP','CZK','DKK','EEK','GBP','HUF','LTL','LVL','MTL','PLN','ROL','RON','SEK','SIT','SKK','CHF','ISK','NOK','HRK','RUB','TRL','TRY','AUD','BRL','CAD','CNY','HKD','IDR','ILS','INR','KRW','MXN','MYR','NZD','PHP','SGD','THB','ZAR')
        self.to_currency_combobox.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)
        self.to_currency_combobox.current(1)

        # Convert button
        self.convert_button = ttk.Button(mainframe, text="Convert", command=self.convert)
        self.convert_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Result label
        self.result_label = ttk.Label(mainframe, text="", font=("Helvetica", 14))
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)

        # Configure column weights
        controller.columnconfigure(0, weight=1)
        controller.rowconfigure(0, weight=1)
        mainframe.columnconfigure(0, weight=1)
        mainframe.columnconfigure(1, weight=1)

    def convert(self):
        amount = float(self.amount_entry.get())
        from_currency = self.from_currency.get()
        to_currency = self.to_currency.get()
        # Adding the data from the currency_converter module
        converted_amount = c.convert(amount, from_currency, to_currency)
        self.result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

if __name__ == "__main__":
    controller = tk.Tk()
    app = CurrencyConverterApp(controller)
    controller.mainloop()
