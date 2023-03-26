from tkinter import *
from PIL import ImageTk, Image


def adder():
    num1 = enter1.get()
    num2 = enter2.get()
    num1 = int(num1)
    num2 = int(num2)
    sum = num1 + num2
    answer.config(text="Answer is =  %s" % (str(sum)))
    answer.place(relx=0.25, rely=0.6)


def subtract():
    num1 = enter1.get()
    num2 = enter2.get()
    num1 = int(num1)
    num2 = int(num2)
    subt = num1 - num2
    answer.config(text="Answer is =  %s" % (str(subt)))
    answer.place(relx=0.25, rely=0.6)


def multiplication():
    num1 = enter1.get()
    num2 = enter2.get()
    num1 = int(num1)
    num2 = int(num2)
    mult = num1 * num2
    answer.config(text="Answer is =  %s" % (str(mult)))
    answer.place(relx=0.25, rely=0.6)


def divide():
    num1 = enter1.get()
    num2 = enter2.get()
    num1 = int(num1)
    num2 = int(num2)
    div = num1 / num2
    answer.config(text="Answer is =  %s" % (str(div)))
    answer.place(relx=0.25, rely=0.6)


window = Tk()
window.title("Calculate")
window.geometry("400x400")
window.iconbitmap("Calculator-icon (1).ico")

window.resizable(False, False)
background = ImageTk.PhotoImage(
    Image.open("HD-wallpaper-microchip-neon-lines-black-background-chips-technology-backgrounds.jpg"))
main_bg = Frame(window).pack(fill=BOTH, expand=True)
Label(main_bg, image=background).pack()

Label(window, text="Enter first number", bg="black", fg="white", font=("Poppins", 12)).place(relx=0.3, rely=0.01)
enter1 = Entry(window, width=30)
enter1.place(relx=0.25, rely=0.1)
Label(window, text="Enter second number", bg="black", fg="white", font=("Poppins", 12)).place(relx=0.26, rely=0.2)
enter2 = Entry(window, width=30)
enter2.place(relx=0.25, rely=0.3)

Button(window, width=3, text="+", font=('Poppins', 12), border=5, command=adder).place(relx=0.20, rely=0.40)
Button(window, width=3, text="-", font=('Poppins', 12), border=5, command=subtract).place(relx=0.35, rely=0.40)
Button(window, width=3, text="x", font=('Poppins', 12), border=5, command=multiplication).place(relx=0.50, rely=0.40)
Button(window, width=3, text="÷", font=('Poppins', 12), border=5, command=divide).place(relx=0.65, rely=0.40)

answer = Label(window, bg="black", fg="white", font=("Poppins", 18))

window.mainloop()
