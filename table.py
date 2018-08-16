import requests
import xml.etree.ElementTree as ET
import tkinter as tk

class TCMBWindow(tk.Frame):

    def __init__(self, master, *args, **kwargs):

        tk.Frame.__init__(self, master, *args, **kwargs)

        table = tk.Frame(self)
        table.pack(side="top", fill="both", expand=True, ipadx=2, ipady=2)
        table.grid_rowconfigure(0, weight=1)
        table.grid_columnconfigure(0, weight=1)
        master.resizable(width=False, height=False)        

        element_tree = ET.ElementTree(ET.fromstring(requests.get("http://tcmb.gov.tr/kurlar/today.xml").text)).getroot()

        self.widgets = {}
        row = 1
                
        tk.Label(table, text="Date: "+element_tree.get("Date")).grid(row=0, column=0, sticky="nsew", padx=5, pady=2)
        tk.Label(table, text="Tarih: "+element_tree.get("Tarih")).grid(row=0, column=1, sticky="nsew", padx=5, pady=2)
        tk.Label(table, text="Bulten No: "+element_tree.get("Bulten_No")).grid(row=0, column=2, sticky="nsew", padx=5, pady=2)
                
        tk.Label(table, text="Currency Code", relief=tk.RIDGE, font=("Helvetica", 10, "bold"), bg="orange").grid(row=1, column=0, sticky="nsew")
        tk.Label(table, text="Unit", relief=tk.RIDGE, font=("Helvetica", 10, "bold"), bg="orange").grid(row=1, column=1, sticky="nsew")
        tk.Label(table, text="Isim", relief=tk.RIDGE, font=("Helvetica", 10, "bold"), bg="orange").grid(row=1, column=2, sticky="nsew")
        tk.Label(table, text="Currency Name", relief=tk.RIDGE, font=("Helvetica", 10, "bold"), bg="orange").grid(row=1, column=3, sticky="nsew")
        tk.Label(table, text="Forex Buying", relief=tk.RIDGE, font=("Helvetica", 10, "bold"), bg="orange").grid(row=1, column=4, sticky="nsew")
        tk.Label(table, text="Forex Selling", relief=tk.RIDGE, font=("Helvetica", 10, "bold"), bg="orange").grid(row=1, column=5, sticky="nsew")
        tk.Label(table, text="Banknote Buying", relief=tk.RIDGE, font=("Helvetica", 10, "bold"), bg="orange").grid(row=1, column=6, sticky="nsew")
        tk.Label(table, text="Banknote Selling", relief=tk.RIDGE, font=("Helvetica", 10, "bold"), bg="orange").grid(row=1, column=7, sticky="nsew")
        
        for currency in element_tree.findall('Currency'):

            row += 1

            currencycode = currency.get('CurrencyCode')
            unit = currency.find('Unit').text
            isim = currency.find('Isim').text
            currencyname = currency.find('CurrencyName').text
            forexbuying = currency.find('ForexBuying').text
            if forexbuying is None: forexbuying = "-"
            forexselling = currency.find('ForexSelling').text
            if forexselling is None: forexselling = "-"
            banknotebuying = currency.find('BanknoteBuying').text
            if banknotebuying is None: banknotebuying = "-"
            banknoteselling = currency.find('BanknoteSelling').text
            if banknoteselling is None: banknoteselling = "-"

            self.widgets[currencycode] = {
                "currencycode": tk.Label(table, text=str(currencycode).strip(), relief=tk.RIDGE),
                "unit": tk.Label(table, text=str(unit).strip(), relief=tk.RIDGE),
                "isim": tk.Label(table, text=str(isim).strip(), relief=tk.RIDGE),        
                "currencyname": tk.Label(table, text=str(currencyname).strip(), relief=tk.RIDGE),
                "forexbuying": tk.Label(table, text=str(forexbuying).strip(), relief=tk.RIDGE),
                "forexselling": tk.Label(table, text=str(forexselling).strip(), relief=tk.RIDGE),
                "banknotebuying": tk.Label(table, text=str(banknotebuying).strip(), relief=tk.RIDGE),
                "banknoteselling": tk.Label(table, text=str(banknoteselling).strip(), relief=tk.RIDGE)
            }

            self.widgets[currencycode]["currencycode"].grid(row=row, column=0, sticky="nsew")
            self.widgets[currencycode]["unit"].grid(row=row, column=1, sticky="nsew")
            self.widgets[currencycode]["isim"].grid(row=row, column=2, sticky="nsew")
            self.widgets[currencycode]["currencyname"].grid(row=row, column=3, sticky="nsew")
            self.widgets[currencycode]["forexbuying"].grid(row=row, column=4, sticky="nsew")
            self.widgets[currencycode]["forexselling"].grid(row=row, column=5, sticky="nsew")
            self.widgets[currencycode]["banknotebuying"].grid(row=row, column=6, sticky="nsew")
            self.widgets[currencycode]["banknoteselling"].grid(row=row, column=7, sticky="nsew")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("TCMB Exchange Rates")
    TCMBWindow(root).pack(fill="both", expand=True)    
    root.mainloop()