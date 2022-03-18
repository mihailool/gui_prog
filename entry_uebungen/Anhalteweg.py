import tkinter as t
import tkinter.ttk as ttk

def on_click_button_1():
    print("Auf den Button geklickt")
    geschwindigkeit = 50
    reaktionsweg = geschwindigkeit / 10 * 3
    label_6.configure(text=reaktionsweg)
    bremsweg = geschwindigkeit / 10 * geschwindigkeit / 10
    label_7.config(text=bremsweg)
    anhalteweg = reaktionsweg + bremsweg
    label_8.config(text=anhalteweg)


fenster = t.Tk()
fenster.title("Anhalteweg")

label_1 = ttk.Label(fenster, text="Geschwindikeit in km/h")
label_1.grid(row=0, column=0)

entry_1 = ttk.Entry(fenster)
entry_1.grid(row=0, column=1)

button_1 = ttk.Button(fenster, text ="Berechnen", command=on_click_button_1)
button_1.grid(row=2, column=0, columnspan=2)

label_2 = ttk.Label(fenster, text="Geschätzter Anhalteweg [in m]")
label_2.grid(row=1, column=0)

entry_2 = ttk.Entry(fenster)
entry_2.grid(row=1, column=1)

label_3 = ttk.Label(fenster, text="Reaktionsweg [in m]")
label_3.grid(row=3, column=0)

label_4 = ttk.Label(fenster, text="Bremsweg [in m]")
label_4.grid(row=4, column=0)

label_5 = ttk.Label(fenster, text="Anhalteweg [in m]")
label_5.grid(row=5, column=0)

label_6 = ttk.Label(fenster, text="???")
label_6.grid(row=3, column=1)

label_7 = ttk.Label(fenster, text="???")
label_7.grid(row=4, column=1)

label_8 = ttk.Label(fenster, text="???")
label_8.grid(row=5, column=1)

fenster.mainloop()

