from tkinter import *


expression = ""
light = "light steel blue"
 


window = Tk()
window.title("Calculator")
window.config(padx=20, pady=20,background=light)
# button_img = PhotoImage(file="button.png")

canvas=Canvas(height=100,width=325)
math = canvas.create_text(250,50,text=f"0",font=("Ariel",20))
canvas.grid(row=0,column=0,columnspan=4,pady=20)

# Creates button objects with predefined parameters
class OperatorButton():
    def __init__(self, value, row, column,func):
        self.value = value
        self.row = row
        self.func = func
        self.column = column
        self.operator = Button(text=value, highlightthickness=0, padx=20,pady=20, width=4,height=2,command=func)
        
        self.operator.grid(row=row,column=column,sticky="ew")
        
# Allows user to change between 1 of 2 color themes
def change_theme():
    global light
    if light == "light steel blue":
        light = "gray"
        window.config(padx=20, pady=20,background=light)
        window.update()
    elif light == "gray":
        light = "light steel blue"
        window.config(padx=20, pady=20,background=light)
        window.update()
    
def equal_press():
    # Try/Except used to catch any expressions that aren't possible
    # such as division errors, etc.
    try:
        global expression
        total = str(eval(expression))
        canvas.itemconfig(math, text = total)
    # if error is generated prints "Error" in calc screen
    except:
        canvas.itemconfig(math, text = "Error")

# Takes button presses and enters them into expression string
def press(num):
    global expression
    expression=expression+str(num)
    canvas.itemconfig(math, text = expression)


# Clears text entry box
def clear_calc():
    global expression
    expression ='0'
    canvas.itemconfig(math, text = expression)

ac_button = OperatorButton("AC",1,1,func=clear_calc)
percent_button = OperatorButton("%",1,2,func=lambda: press('%'))
nine_button = OperatorButton("9",2,2,func=lambda: press(9))
eight_button = OperatorButton("8",2,1,func=lambda: press(8))
seven_button = OperatorButton("7",2,0,func=lambda: press(7))
six_button = OperatorButton("6",3,2,func=lambda: press(6))
five_button = OperatorButton("5",3,1,func=lambda: press(5))
four_button = OperatorButton("4",3,0,func=lambda: press(4))
three_button = OperatorButton("3",4,2,func=lambda: press(3))
two_button = OperatorButton("2",4,1,func=lambda: press(2))
one_button = OperatorButton("1",4,0,func=lambda: press(1))
zero_button = OperatorButton("0",5,0,func=lambda: press(0))
period_button = OperatorButton(".",5,1,func=lambda: press('.'))
equals_button = OperatorButton("=",5,2,func=equal_press)
divide_button = OperatorButton("÷",1,3,func=lambda: press('/'))
multiply_button = OperatorButton("x",2,3,func=lambda: press('*'))
subtract_button = OperatorButton("-",3,3,func=lambda: press('-'))
plus_button = OperatorButton("+",4,3,func=lambda: press('+'))
theme_button = OperatorButton("THEME",5,3,func=change_theme)


window.mainloop()