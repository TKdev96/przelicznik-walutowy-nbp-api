from tkinter import *
import tkinter as tk
import requests
import json
from tkcalendar import DateEntry 
from csv import writer

frame = tk.Tk()
frame.title("Przelicznik walut")
frame.geometry('400x400')

def printInput():
   inpA = a1.get_date()
   lbl1.config(text = "Data (RRRR-MM-DD): "+str(inpA))
   inpB = b1.get(1.0, "end-1c")
   lbl2.config(text = "Kod waluty (eur / usd / gbp): "+inpB)

   inpC = c1.get(1.0, "end-1c")
   lbl3.config(text = "Kwota na fakturze: "+inpC)

   inpCToInt = int(inpC)

   url = f"http://api.nbp.pl/api/exchangerates/rates/a/{inpB}/{inpA}/"
   r = requests.get(url)
   res = r.json()
   
   for i in res['rates']:
      items = i
      

   wynikWaluta = res['code']
   wynikKurs = (items['mid'])

   wynik = int(inpCToInt * wynikKurs)
   lbl4.config(text = f"Wartość faktury po przeliczeniu: {wynik} ")

   dane = [inpA, wynikWaluta, wynikKurs, wynik] 
   with open('wprowadzone_faktury.csv', 'a') as f:
      writer_object = writer(f)
      writer_object.writerow(dane)
      f.close()


data = Label(text="Data: ") 
data.pack()
a1 = DateEntry(frame, selectmode='day')
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
