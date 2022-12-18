import tkinter as tk

win = tk.Tk()
win.geometry(f"240x260+100+200")
win['bg'] = '#808080'
win.title("Калькултор")

calc = tk.Entry(win)
calc.grid(row=0, column=0, columnspan=3)

tk.Button(text='1', ).grid(row=1, column=1)
tk.Button(text='2', ).grid(row=1, column=2)
tk.Button(text='3', ).grid(row=1, column=3)
tk.Button(text='4', ).grid(row=2, column=1)
tk.Button(text='5', ).grid(row=2, column=2)
tk.Button(text='6', ).grid(row=2, column=3)
tk.Button(text='7', ).grid(row=3, column=1)
tk.Button(text='8', ).grid(row=3, column=2)
tk.Button(text='9', ).grid(row=3, column=3)
tk.Button(text='0', ).grid(row=4, column=2)

win.grid_columnconfigure(0,minisize=60)
win.grid_columnconfigure(2,minisize=60)
win.grid_columnconfigure(3,minisize=60)

win.grid_rowconfigure(0,minisize=60)
win.grid_rowconfigure(2,minisize=60)
win.grid_rowconfigure(3,minisize=60)


win.mainloop()
