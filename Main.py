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
typeOfProblem = StringVar()
listOfConstraints=[]
listOfVariables = []
listOfLowerBounds = []
nameOfProblem = StringVar()
objectiveFunction = StringVar()



Label(canvas, text='Number of constraints', font='SAN_SERIF 12').place(x=240, y=30)
Entry(canvas, width=55, textvariable=numberOfConstraints, justify=CENTER).place(x=240, y=60)

Label(canvas, text='Maximization or Minimization:', font='SAN_SERIF 12').place(x=240, y=120)
Entry(canvas, width=55, textvariable=typeOfProblem, justify=CENTER).place(x=240, y=150)


def set_variables():
    if ((not numberOfConstraints.get()) or (not typeOfProblem.get())):
        messagebox.showinfo('Error', 'Text boxes can\'t be left empty')
        return
    elif (typeOfProblem.get().lower() != 'maximization' and typeOfProblem.get().lower() != 'minimization'):
        messagebox.showinfo('Error', 'Problem can either be of type Maximization or Minimization')
    else:
        try:
            int(numberOfConstraints.get())
        except ValueError:
            messagebox.showinfo('Error', 'Number of constraints must be an integer value')


    #url = str(numberOfConstraints.get())



tkinter.Button(canvas, text='Confirm',
               command=set_variables, font=('SAN_SERIF', 15, 'bold'), relief=FLAT,
               activebackground='black', activeforeground='white').place(x=300, y=300)

canvas.mainloop()