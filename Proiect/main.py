from scraper import trade_spider
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def convert_to():
    options = trade_spider()
    flag = 0
    initial_currency = variable1.get()
    final_currency = variable2.get()
    if initial_currency == 'None':
        messagebox.showerror("Error input 1", "You did not choose the currency type !!!")
        flag = 1
    if final_currency == 'None':
        messagebox.showerror("Error input 2", "You did not choose the currency type !!!")
        flag = 1
    try:    
        input_price = float(input_value.get('1.0',END))
    except:
        messagebox.showerror("Error input 3", "This number does not exist (use . no ,) !!!")
        flag = 1
    if flag == 0:
        final_price = input_price * options[initial_currency]
        final_price = final_price / options[final_currency]
        output_value.delete('1.0', END)
        output_value.insert(END, str(final_price))           


converter = Tk()
converter.title("Unit Converter")
converter.geometry("800x400")
converter.config(bg="#f1e4d3")
options = trade_spider()
appName = Label(converter,text="Currency Converter",font = ("Comic Sans MS", 30, "bold"),fg="#5b7771", bg="#f1e4d3")
appName.place(x=215, y=10)

variable1 = StringVar(converter)
variable1.set(None)

input_options = OptionMenu(converter,variable1,*options)
input_options.place(x= 100 , y=150,width=300, height=50)
input_options.config(bg = "#5b7771",fg = "#402e20",font=("Comic Sans MS",15,"bold"), activebackground = "#bfb48d" )

input_value = Text(converter,height=1,width=15,font=("arial",20,"bold"),bd=5)
input_value.config(bg = "#5b7771", fg = "#402e20")
input_value.place(x=130, y=250)

variable2 = StringVar(converter)
variable2.set(None)

output_options = OptionMenu(converter,variable2,*options)
output_options.place(x= 400 , y=150,width=300, height=50)
output_options.config(bg = "#5b7771",fg = "#402e20",font=("Comic Sans MS",15,"bold"), activebackground = "#bfb48d" )

output_value = Text(converter,height=1,width=15,font=("arial",20,"bold"),bd=5)
output_value.config(bg = "#5b7771", fg = "#402e20")
output_value.place(x = 425, y = 250)

convert_button = Button(converter, text = "convert", bd = 5, command = convert_to)
convert_button.config(bg = "#5b7771",fg = "#402e20",font=("Comic Sans MS",20,"bold"), activebackground = "#bfb48d")
convert_button.place(x = 330, y = 320)

converter.mainloop()