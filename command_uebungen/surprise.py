import tkinter as t
import tkinter.ttk as ttk

def on_click_button_1():
    label_1.config(text="KSWE")
    label_2.config(text="2021")

fenster = t.Tk()
fenster.title("Surprise")

label_1 = ttk.Label(fenster, text="???")
label_1.grid (row=0, column=0)

label_2 = ttk.Label(fenster, text="???")
label_2.grid (row=0, column=2)

button_1 = ttk.Button (fenster, text="Surprise", command=on_click_button_1)
button_1.grid (row=1, column=0)

fenster.mainloop()