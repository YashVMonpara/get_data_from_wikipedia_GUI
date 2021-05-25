import tkinter as tk
from tkinter.messagebox import showinfo, showerror
import wikipedia

win = tk.Tk()
win.title('Wikipedia Search')


def get_data():
    query = entry1.get()
    if query == '':
        showerror('Error', 'Please enter query')
    else:
        showinfo('Result', wikipedia.summary(query))


label1 = tk.Label(win, text='Your query: ')
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(win, width=35)
entry1.grid(row=0, column=1, pady=10, padx=10)

btn = tk.Button(win, text="Search", command=get_data, borderwidth=1)
btn.grid(row=1, column=0, columnspan=2, pady=10)

win.mainloop()
