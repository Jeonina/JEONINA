from tkinter import *

window = None
result_label = None
expression = ''


# define functions
def press(x):
    global result_label
    global expression
    expression = expression + str(x)
    result_label['text'] = expression


def press_back():
    global result_label
    global expression
    expression = expression[:-1]
    result_label['text'] = expression


def press_square():
    global result_label
    global expression
    expression = expression + str('²')
    result_label['text'] = expression


def press_root():
    global result_label
    global expression
    expression = expression + str('½')
    result_label['text'] = expression


def press_change():
    global result_label
    global expression
    expression = str(eval(expression) * -1)
    result_label['text'] = expression


def press_mul():
    global result_label
    global expression
    expression = expression + '×'
    result_label['text'] = expression


def press_div():
    global result_label
    global expression
    expression = expression + '÷'
    result_label['text'] = expression


def press_percent():
    global result_label
    global expression
    expression = expression + str('%')
    result_label['text'] = expression


def press_clear():
    global result_label
    global expression
    expression = ''
    result_label['text'] = '0'


def press_result():
    global expression
    global result_label
    try:
        expression = expression.replace('²', '**2')
        expression = expression.replace('÷', '/')
        expression = expression.replace('×', '*')
        expression = expression.replace('½', '**(1/2)')
        expression = expression.replace('%', '*0.01')
        total = str(eval(expression))
        result_label['text'] = total[:15]
    except:
        result_label['text'] = 'Error'
    expression = ''


# define functions by using keyboards
def keyboard_result(e):
    global expression
    global result_label
    try:
        expression = expression.replace('²', '**2')
        expression = expression.replace('÷', '/')
        expression = expression.replace('×', '*')
        expression = expression.replace('½', '**(1/2)')
        expression = expression.replace('%', '*0.01')
        total = str(eval(expression))
        result_label['text'] = total[:15]
    except:
        result_label['text'] = 'Error'
    expression = ''


def keyboard_back(e):
    global result_label
    global expression
    expression = expression[:-1]
    result_label['text'] = expression


def keyboard_mul(e):
    global result_label
    global expression
    expression = expression + '×'
    result_label['text'] = expression


def keyboard_div(e):
    global result_label
    global expression
    expression = expression + '÷'
    result_label['text'] = expression


def keyboard_add(e):
    global result_label
    global expression
    expression = expression + '+'
    result_label['text'] = expression


def keyboard_sub(e):
    global result_label
    global expression
    expression = expression + '-'
    result_label['text'] = expression


def keyboard1(e):
    global result_label
    global expression
    expression = expression + '1'
    result_label['text'] = expression


def keyboard2(e):
    global result_label
    global expression
    expression = expression + '2'
    result_label['text'] = expression


def keyboard3(e):
    global result_label
    global expression
    expression = expression + '3'
    result_label['text'] = expression


def keyboard4(e):
    global result_label
    global expression
    expression = expression + '4'
    result_label['text'] = expression


def keyboard5(e):
    global result_label
    global expression
    expression = expression + '5'
    result_label['text'] = expression


def keyboard6(e):
    global result_label
    global expression
    expression = expression + '6'
    result_label['text'] = expression


def keyboard7(e):
    global result_label
    global expression
    expression = expression + '7'
    result_label['text'] = expression


def keyboard8(e):
    global result_label
    global expression
    expression = expression + '8'
    result_label['text'] = expression


def keyboard9(e):
    global result_label
    global expression
    expression = expression + '9'
    result_label['text'] = expression


def keyboard0(e):
    global result_label
    global expression
    expression = expression + '0'
    result_label['text'] = expression


def keyboard_dot(e):
    global result_label
    global expression
    expression = expression + 'ㆍ'
    result_label['text'] = expression


# define GUI
def GUI():
    global window
    global result_label
    window = Tk()
    window.title('Calculator')
    window.resizable(False, False)
    result_label = Label(window, text='', relief=SUNKEN, borderwidth = 3, pady=8, anchor='e', width=15, font='Courier 23')
    result_label.grid(row=0, column=0, columnspan=4)

# set the buttons
    btn1 = Button(window, text='1', width=5, height=2, activebackground='grey', bg='white', font='굴림체 20', command=lambda: press(1))
    btn2 = Button(window, text='2', width=5, height=2, activebackground='grey', bg='white', font='굴림체 20', command=lambda: press(2))
    btn3 = Button(window, text='3', width=5, height=2, activebackground='grey', bg='white', font='굴림체 20', command=lambda: press(3))
    btn4 = Button(window, text='4', width=5, height=2, activebackground='grey', bg='white', font='굴림체 20', command=lambda: press(4))
    btn5 = Button(window, text='5', width=5, height=2, activebackground='grey', bg='white', font='굴림체 20', command=lambda: press(5))
    btn6 = Button(window, text='6', width=5, height=2, activebackground='grey', bg='white', font='굴림체 20', command=lambda: press(6))
    btn7 = Button(window, text='7', width=5, height=2, activebackground='grey', bg='white', font='굴림체 20', command=lambda: press(7))
    btn8 = Button(window, text='8', width=5, height=2, activebackground='grey', bg='white', font='굴림체 20', command=lambda: press(8))
    btn9 = Button(window, text='9', width=5, height=2, activebackground='grey', bg='white', font='굴림체 20', command=lambda: press(9))
    btn0 = Button(window, text='0', width=5, height=2, activebackground='grey', bg='white', font='굴림체 20', command=lambda: press(0))
    btnbl = Button(window, text='(', width=5, height=2, activebackground='grey', font='굴림체 20', command=lambda: press("("))
    btnbr = Button(window, text=')', width=5, height=2, activebackground='grey', font='굴림체 20', command=lambda: press(")"))
    btndot = Button(window, text='.', width=5, height=2, activebackground='grey', bg='white', font='굴림체 20', command=lambda: press("ㆍ"))
    add_btn = Button(window, text='+', width=5, height=2, activebackground='grey', font='굴림체 20', command=lambda: press('+'))
    sub_btn = Button(window, text='-', width=5, height=2, activebackground='grey', font='굴림체 20', command=lambda: press('-'))
    mul_btn = Button(window, text='×', width=5, height=2, activebackground='grey', font='굴림체 20', command=press_mul)
    div_btn = Button(window, text='÷', width=5, height=2, activebackground='grey', font='굴림체 20', command=press_div)
    clear_btn = Button(window, text='C', width=5, height=2, activebackground='grey', fg='red', font='굴림체 20', command=press_clear)
    result_btn = Button(window, text='=', width=5, height=2, activeforeground='red', bg='grey', font='굴림체 20', command=press_result)
    back_btn = Button(window, text='Back', width=5, height=2, activebackground='grey', font='굴림체 20', command=press_back)
    root_btn = Button(window, text='√', width=5, height=2, activebackground='grey', font='굴림체 20', command=press_root)
    square_btn = Button(window, text='  X²', width=5, height=2, activebackground='grey', font='굴림체 20', command=press_square)
    percent_btn = Button(window, text='%', width=5, height=2, activebackground='grey', font='굴림체 20', command=press_percent)
    change_btn = Button(window, text='+/-', width=5, height=2, activebackground='grey', bg='white', font='굴림체 20', command=press_change)

# and... the positions of buttons
    btn1.grid(row=2, column=0)
    btn2.grid(row=2, column=1)
    btn3.grid(row=2, column=2)
    btn4.grid(row=3, column=0)
    btn5.grid(row=3, column=1)
    btn6.grid(row=3, column=2)
    btn7.grid(row=4, column=0)
    btn8.grid(row=4, column=1)
    btn9.grid(row=4, column=2)
    btn0.grid(row=5, column=1)
    btnbl.grid(row=6, column=0)
    btnbr.grid(row=6, column=1)
    btndot.grid(row=5, column=2)
    add_btn.grid(row=2, column=3)
    sub_btn.grid(row=3, column=3)
    mul_btn.grid(row=4, column=3)
    div_btn.grid(row=5, column=3)
    clear_btn.grid(row=6, column=2)
    result_btn.grid(row=6, column=3)
    back_btn.grid(row=1, column=3)
    root_btn.grid(row=1, column=2)
    square_btn.grid(row=1, column=1)
    percent_btn.grid(row=1, column=0)
    change_btn.grid(row=5, column=0)

# bind keyboard-functions with calculator
    window.bind('<Return>', keyboard_result)
    window.bind('<BackSpace>', keyboard_back)
    window.bind('<KeyPress-*>', keyboard_mul)
    window.bind('<KeyPress-/>', keyboard_div)
    window.bind('<KeyPress-+>', keyboard_add)
    window.bind('<KeyPress-->', keyboard_sub)
    window.bind('<KeyPress-1>', keyboard1)
    window.bind('<KeyPress-2>', keyboard2)
    window.bind('<KeyPress-3>', keyboard3)
    window.bind('<KeyPress-4>', keyboard4)
    window.bind('<KeyPress-5>', keyboard5)
    window.bind('<KeyPress-6>', keyboard6)
    window.bind('<KeyPress-7>', keyboard7)
    window.bind('<KeyPress-8>', keyboard8)
    window.bind('<KeyPress-9>', keyboard9)
    window.bind('<KeyPress-0>', keyboard0)
    window.bind('<KeyPress-.>', keyboard_dot)

GUI()
window.mainloop()