from tkinter import *
from tkinter import ttk

root = Tk()
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=3)
root.columnconfigure(2, weight=1)
    
ttk.Label(root, text='yellow', background='yellow').grid(row=0, column=2, rowspan=2, sticky='nsew')
ttk.Label(root, text='blue', background='blue').grid(row=1, column=0, columnspan=2, sticky='nsew')
ttk.Label(root, text='green', background='green').grid(row=0, column=0, sticky='nsew', padx=10)
ttk.Label(root, text='orange', background='orange').grid(row=0, column=1, sticky='nsew', ipadx=25, ipady=25)

root.mainloop()
