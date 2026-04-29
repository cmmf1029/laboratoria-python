# #zadanie 1
# import tkinter as tk
# from tkinter import messagebox
# def calculate():
#     try:
#         a = float(entry1.get())
#         b = float(entry2.get())
#         op = operation.get()
#         if op == 1:
#             result = a + b
#         elif op == 2:
#             result = a - b
#         elif op == 3:
#             result = a * b
#         elif op == 4:
#             result = a / b
#         else:
#             result = "Brak operacji"
#         messagebox.showinfo("Wynik", f"Wynik: {result}")
#     except ValueError:
#         messagebox.showerror("Błąd", "TypeError: wpisz liczby!")
#     except ZeroDivisionError:

#zadanie 2
import tkinter as tk
from tkinter import messagebox
def oblicz_rate():
    try:
        K = float(entry_k.get())
        n = int(entry_n.get())
        p = float(entry_p.get())
        if K < 1000 or K > 10000:
            messagebox.showerror("Błąd", "Kwota K musi być 1000–10000.")
            return
        if n not in [1, 2, 3]:
            messagebox.showerror("Błąd", "n musi być 1, 2 lub 3.")
            return

        q = 1 + p / 100
        rata = (K * (q ** n) * (1 - q)) / (1 - (q ** n))

        wynik_label.config(text=f"Rata: {rata:.2f} zł")
        if rata < 500:
            wynik_label.config(fg="green")
        elif rata < 1500:
            wynik_label.config(fg="orange")
        else:
            wynik_label.config(fg="red")
    except ValueError:
        messagebox.showerror("Błąd", "Wpisz poprawne liczby!")

root = tk.Tk()
root.title("Kalkulator raty kredytu")
tk.Label(root, text="Kwota K:").pack()
entry_k = tk.Entry(root)
entry_k.pack()
tk.Label(root, text="Liczba okresów n (1-3):").pack()
entry_n = tk.Entry(root)
entry_n.pack()
tk.Label(root, text="Stopa procentowa p (%):").pack()
entry_p = tk.Entry(root)
entry_p.pack()
tk.Button(root, text="Oblicz ratę", command=oblicz_rate).pack()
wynik_label = tk.Label(root, text="Rata: ---", font=("Arial", 14))
wynik_label.pack()
root.mainloop()


#zadanie 3
import tkinter as tk
from tkinter import messagebox
def pokaz_wynik():
    wybor = []
    if var1.get() == 1:
        wybor.append("AGD")
    if var2.get() == 1:
        wybor.append("Kosmetyki")
    if var3.get() == 1:
        wybor.append("Odzież")
    if not wybor:
        messagebox.showinfo("Wynik", "Nic nie wybrano.")
    else:
        messagebox.showinfo("Wynik", "Wybrałeś: " + ", ".join(wybor))
root = tk.Tk()
root.title("Ankieta świąteczna")
tk.Label(root, text="Co najczęściej kupujesz w prezencie?").pack()
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
tk.Checkbutton(root, text="AGD", variable=var1).pack()
tk.Checkbutton(root, text="Kosmetyki", variable=var2).pack()
tk.Checkbutton(root, text="Odzież", variable=var3).pack()
tk.Button(root, text="OK", command=pokaz_wynik).pack()
root.mainloop()
