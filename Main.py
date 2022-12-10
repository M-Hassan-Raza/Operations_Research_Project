from tkinter import *
import tkinter
from tkinter import messagebox

canvas = Tk()
canvas.geometry("800x600")
canvas.title("Linear Programming Solver")
canvas.iconbitmap('res/line-chart.ico')
canvas.configure(bg='white')
canvas.resizable(False, False)

numberOfConstraints = StringVar()
typeOfProblem = StringVar()


Label(canvas, text='Number of constraints', font='SAN_SERIF 12').place(x=260, y=30)
link_enter = Entry(canvas, width=55, textvariable=numberOfConstraints, justify=CENTER).place(x=280, y=60)

Label(canvas, text='Maximization or Minimization:', font='SAN_SERIF 12').place(x=260, y=120)
link_enter = Entry(canvas, width=55, textvariable=typeOfProblem, justify=CENTER).place(x=280, y=150)


def set_variables():
    if not numberOfConstraints.get():
        return

    url = str(numberOfConstraints.get())
    messagebox.showinfo(
        "Information", "Download Successful! Output placed in the Source folder")


tkinter.Button(canvas, text="Confirm",
               command=set_variables, font=("SAN_SERIF", 15, "bold"), relief=FLAT,
               activebackground="black", activeforeground="white").place(x=170, y=200)

canvas.mainloop()