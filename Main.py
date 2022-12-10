from tkinter import *
import tkinter
from tkinter import messagebox

canvas = Tk()
canvas.geometry('800x600')
canvas.title('Linear Programming Solver')
canvas.iconbitmap('res/line-chart.ico')
canvas.configure(bg='pink')
canvas.resizable(False, False)

numberOfConstraints = StringVar()
intConstraints = 0
typeOfProblem = StringVar()
listOfConstraints = []
listOfDecisionVariables = []
listOfLowerBounds = []
listOfUpperBounds = []
nameOfProblem = StringVar()
objectiveFunction = StringVar()
problem = StringVar()

Label(canvas, text='Number of constraints', font='SAN_SERIF 12').place(x=240, y=30)
Entry(canvas, width=55, textvariable=numberOfConstraints, justify=CENTER).place(x=240, y=60)

Label(canvas, text='Maximization or Minimization:', font='SAN_SERIF 12').place(x=240, y=120)
Entry(canvas, width=55, textvariable=typeOfProblem, justify=CENTER).place(x=240, y=150)


def main_function():
    if (not numberOfConstraints.get()) or (not typeOfProblem.get()):
        messagebox.showinfo('Error', 'Text boxes can\'t be empty')
        return
    elif typeOfProblem.get().lower() != 'maximization' and typeOfProblem.get().lower() != 'minimization':
        messagebox.showinfo('Error', 'Problem can either be of type Maximization or Minimization')
        return
    else:
        try:
            int(numberOfConstraints.get())
            intConstraints = int(numberOfConstraints.get())
        except ValueError:
            messagebox.showinfo('Error', 'Number of constraints must be an integer value')
            return

    top = Toplevel()
    top.geometry('800x600')
    top.title('Enter The Data')
    top.iconbitmap('res/form.ico')
    top.configure(bg='pink')
    top.resizable(False, False)

    l = Label(top, text='Objective Function: ')
    l.grid(row=0, column=0, padx=50, pady=10)
    e = Entry(top)
    e.grid(row=0, column=1, padx=10, pady=10)

    for j in range(intConstraints):
        l = Label(top, text='Constraint: ' + str(j + 1))
        l.grid(row=j + 1, column=0, padx=10)

        e = Entry(top)
        e.grid(row=j + 1, column=1, padx=10, pady=10)

    Button(top, text='Confirm',
                   command=main_function, font=('SAN_SERIF', 15, 'bold'), relief=FLAT,
                   activebackground='black', activeforeground='white').place(x=300, y=300)

tkinter.Button(canvas, text='Confirm',
               command=main_function, font=('SAN_SERIF', 15, 'bold'), relief=FLAT,
               activebackground='black', activeforeground='white').place(x=300, y=300)

canvas.mainloop()
