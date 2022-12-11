from tkinter import *
from tkinter import ttk



a = 0
b = 0
# last_action = ''
# is_new_number = True
#
#
# def set_text(num):
#     global is_new_number
#
#     temp = text_space.cget("text")
#
#     if temp != '0' and not is_new_number:
#         text_space.config(text=temp + num)
#         is_new_number = False
#     else:
#         text_space.config(text=num)
#         is_new_number = False
#
#
# def action(sign):
#     global a
#     global last_action
#     global is_new_number
#
#     if sign != '=':
#         a = text_space.cget('text')
#         set_text(a)
#         # set_text('')
#         last_action = sign
#         is_new_number = True
#         if sign == "+":
#             text_space.config(text=int(a) + int(text_space.cget('text')))
#         if sign == "-":
#             text_space.config(text=int(a) - int(text_space.cget('text')))
#         if sign == "/":
#             text_space.config(text=int(a) / int(text_space.cget('text')))
#         if sign == "*":
#             text_space.config(text=int(a) * int(text_space.cget('text')))
#
#     else:
#         print('something went wrong')
def add_digit(digit):
    text_space.insert(0, digit)


def clear():
    text_space.delete(0, END)


def clear_1_simbol():
    text_space.delete(text_space.index(END) - 1)

# def actions_for_2_digits(sign):
#     if sign == "*":
#         a =

# def test_func():
#     test_space.delete(tsxt_space.index(0), '=')

root = Tk()
root.title('Calc tkinter ver')
root.geometry('300x350+500+200')

s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 16), background="#000000")

text_space = Entry(text='0', font='Arial 24')
text_space.place(relx=0, rely=0,
                 relwidth=1, relheight=0.2)

btn_frame = ttk.Frame(relief=GROOVE, )
btn_frame.place(relx=0, rely=0.2,
                relwidth=1, relheight=0.8)

CE_btn = ttk.Button(btn_frame, text='CE', command = clear, style = 'my.TButton')
CE_btn.place(relx=0, rely=0.0,
             relwidth=0.25, relheight=0.2)

C_btn = ttk.Button(btn_frame, text='C', command=clear_1_simbol,style='my.TButton')
C_btn.place(relx=0.25, rely=0.0,
            relwidth=0.25, relheight=0.2)

BS_btn = ttk.Button(btn_frame, text='BS',style='my.TButton')
BS_btn.place(relx=0.5, rely=0.0,
             relwidth=0.25, relheight=0.2)

div_btn = ttk.Button(btn_frame, text='/', style='my.TButton',
                     command=lambda: actions_for_2_digits('*'))
div_btn.place(relx=0.75, rely=0.0,
              relwidth=0.25, relheight=0.2)

n7_btn = ttk.Button(btn_frame, text='7', style='my.TButton',
                    command=lambda: add_digit(7))
n7_btn.place(relx=0.0, rely=0.2,
             relwidth=0.25, relheight=0.2)

n8_btn = ttk.Button(btn_frame, text='8', style='my.TButton',
                    command=lambda: add_digit(8))
n8_btn.place(relx=0.25, rely=0.2,
             relwidth=0.25, relheight=0.2)

n9_btn = ttk.Button(btn_frame, text='9', style='my.TButton',
                    command=lambda: add_digit(9))
n9_btn.place(relx=0.5, rely=0.2,
             relwidth=0.25, relheight=0.2)

mul_btn = ttk.Button(btn_frame, text='*', style='my.TButton',
                     command=lambda: ation('*'))
mul_btn.place(relx=0.75, rely=0.2,
              relwidth=0.25, relheight=0.2)

n4_btn = ttk.Button(btn_frame, text='4', style='my.TButton',
                    command=lambda: add_digit(4))
n4_btn.place(relx=0.0, rely=0.4,
             relwidth=0.25, relheight=0.2)

n5_btn = ttk.Button(btn_frame, text='5', style='my.TButton',
                    command=lambda: add_digit(5))
n5_btn.place(relx=0.25, rely=0.4,
             relwidth=0.25, relheight=0.2)

n6_btn = ttk.Button(btn_frame, text='6', style='my.TButton',
                    command=lambda: add_digit(6))
n6_btn.place(relx=0.5, rely=0.4,
             relwidth=0.25, relheight=0.2)

plus_btn = ttk.Button(btn_frame, text='+', style='my.TButton',
                      command=lambda: action('+'))
plus_btn.place(relx=0.75, rely=0.4,
               relwidth=0.25, relheight=0.2)

equal_btn = ttk.Button(btn_frame, text='=', style='my.TButton',
                       command=lambda: action('='))
equal_btn.place(relx=0.75, rely=0.6,
                relwidth=0.25, relheight=0.2)




n1_btn = ttk.Button(btn_frame, text='1', style='my.TButton',
                    command=lambda: add_digit(4))
n1_btn.place(relx=0.0, rely=0.6,
             relwidth=0.25, relheight=0.2)

n2_btn = ttk.Button(btn_frame, text='2', style='my.TButton',
                    command=lambda: add_digit(5))
n2_btn.place(relx=0.25, rely=0.6,
             relwidth=0.25, relheight=0.2)

n3_btn = ttk.Button(btn_frame, text='3', style='my.TButton',
                    command=lambda: add_digit(3))
n3_btn.place(relx=0.5, rely=0.6,
             relwidth=0.25, relheight=0.2)













# rand_btn = ttk.Button(btn_frame, text=' ', style='my.TButton',
#                        command=lambda: test_func())
# rand_btn.place(relx=0.0, rely=0.8,
#                 relwidth=0.25, relheight=0.2)


"""
max = 28
for y in range(0, 5):
    for x in range(1, 8):
        if (x+y*7) <= max:
            print(x+y*7, ',', end='')
    print()
"""

root.mainloop()
