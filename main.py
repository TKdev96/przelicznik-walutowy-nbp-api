from tkinter import *
import tkinter as tk
import requests
import json


frame = tk.Tk()
frame.title("Przelicznik walut")
frame.geometry('400x400')

def printInput():
   inpA = a1.get(1.0, "end-1c")
   lbl1.config(text = "Data (RRRR-MM-DD): "+inpA)
   
   inpB = b1.get(1.0, "end-1c")
   lbl2.config(text = "Kod waluty (eur / usd / gbp): "+inpB)

   inpC = c1.get(1.0, "end-1c")
   lbl3.config(text = "Kwota na fakturze: "+inpC)

   inpCToInt = int(inpC)


   print(type(inpA), type(inpB), type(inpC))

   url = f"http://api.nbp.pl/api/exchangerates/rates/a/{inpB}/{inpA}/"
   print(url)
   r = requests.get(url)
   print(type(r))
   res = r.json()
   print(type(res))
   

   for i in res['rates']:
      items = i
      print(i)

   wynikWaluta = res['code']
   wynikKurs = (items['mid'])
   print(wynikWaluta, wynikKurs)
   print(type(wynikKurs))

   wynik = float(inpCToInt * wynikKurs)
   lbl4.config(text = f"Wartość faktury po przeliczeniu: {wynik} ")





data = Label(text="Data (RRRR-MM-DD): ") 
data.pack()
a1 = tk.Text(frame, height=2, width=10)
a1.pack()

waluta = Label(text="Kod waluty (eur / usd / gbp): ")
waluta.pack()
b1 = tk.Text(frame, height=2, width=10)
b1.pack()

faktura = Label(text="Kwota na fakturze: ")
faktura.pack()
c1 = tk.Text(frame, height=2, width=10)
c1.pack()



printButton = tk.Button(frame, text="Przelicz", command=printInput)
printButton.pack()

lbl1 = tk.Label(frame, text = "")
lbl1.pack()

lbl2 = tk.Label(frame, text = "")
lbl2.pack()

lbl3 = tk.Label(frame, text = "")
lbl3.pack()

lbl4 = tk.Label(frame, text = "")
lbl4.pack()



frame.mainloop()