from tkinter import *

window = Tk()
window.geometry('500x354')
window.title('Calculator')
window.resizable(False, False)


def click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


def clear():
    global expression
    expression = ''
    input_text.set('')


def equal():
    try:
        global expression
        result = str(eval(expression))
        input_text.set(result)
        expression = ''
    except Exception:
        expression = ''
        input_text.set('Error! Please click C button')


# Input text
expression = ''
input_text = StringVar()
input_frame = Frame(window, width=312, height=50, bg='#f0f0f0')
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bd=0, insertwidth=4,
                    bg='#eee', justify=RIGHT)
input_field.grid(row=0, column=0)
input_field.pack()

# Buttons
frame_buttons = Frame(window, width=500, height=304, bg='grey')
frame_buttons.pack()

button_clear = Button(frame_buttons, text='C', height=3, width=32, bd=0, bg='#eee', cursor='hand2',
                      command=lambda: clear())
button_clear.grid(row=0, column=0, columnspan=3)

divide = Button(frame_buttons, text='/', height=3, width=10, bd=0, bg='#FFA500', cursor='hand2', command=lambda: click('/'))
divide.grid(row=0, column=3)

seven = Button(frame_buttons, text='7', height=3, width=10, bg='#eee', cursor='hand2', command=lambda: click('7'))
seven.grid(row=1, column=0)

eight = Button(frame_buttons, text='8', height=3, width=10, bg='#eee', cursor='hand2',
               command=lambda: click('8'))
eight.grid(row=1, column=1)
nine = Button(frame_buttons, text='9', height=3, width=10, bg='#eee', cursor='hand2',
              command=lambda: click('9'))
nine.grid(row=1, column=2)

four = Button(frame_buttons, text='4', height=3, width=10, bg='#eee', cursor='hand2',
              command=lambda: click('4'))
four.grid(row=2, column=0)

five = Button(frame_buttons, text='5', height=3, width=10, bg='#eee', cursor='hand2',
              command=lambda: click('5'))
five.grid(row=2, column=1)

six = Button(frame_buttons, text='6', height=3, width=10, bg='#eee', cursor='hand2', command=lambda: click('6'))
six.grid(row=2, column=2)

multiply = Button(frame_buttons, text='*', height=3, width=10, bg='#eee', cursor='hand2', command=lambda: click('*'))
multiply.grid(row=1, column=3)

one = Button(frame_buttons, text='1', height=3, width=10, bg='#eee', cursor='hand2', command=lambda: click('1'))
one.grid(row=3, column=0)

two = Button(frame_buttons, text='2', height=3, width=10, bg='#eee', cursor='hand2', command=lambda: click('2'))
two.grid(row=3, column=1)

three = Button(frame_buttons, text='3', height=3, width=10, bg='#eee', cursor='hand2', command=lambda: click('3'))
three.grid(row=3, column=2)

plus = Button(frame_buttons, text='+', height=3, width=10, bg='#eee', cursor='hand2',
              command=lambda: click('+'))
plus.grid(row=3, column=3)

minus = Button(frame_buttons, text='-', height=3, width=10, bg='#eee', cursor='hand2',
               command=lambda: click('-'))
minus.grid(row=2, column=3)

zero = Button(frame_buttons, text='0', height=3, width=10, bg='#eee', cursor='hand2',
              command=lambda: click('0'))
zero.grid(row=4, column=1)

virgula = Button(frame_buttons, text='.', height=3, width=10, bg='#eee', cursor='hand2',
                 command=lambda: click('.'))
virgula.grid(row=4, column=2)

egal = Button(frame_buttons, text='=', height=3, width=10, bg='#eee', cursor='hand2',
              command=lambda: equal())
egal.grid(row=4, column=3)

zerozero = Button(frame_buttons, text='00', height=3, width=10, bg='#eee', cursor='hand2',
                  command=lambda: equal())
zerozero.grid(row=4, column=0)

window.mainloop()
