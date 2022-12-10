from tkinter import *
import tkinter
from tkinter import messagebox
import customtkinter

canvas = customtkinter.CTk()
canvas.geometry('800x600')
canvas.title('Linear Programming Solver')
canvas.iconbitmap('res/line-chart.ico')
canvas.resizable(False, False)
customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("light")


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


# menubar = Menu(canvas)
# canvas.config(menu=menubar)
# about_menu =
# about_menu.add_command(label='About', command=show_about_menu)


constLabel = customtkinter.CTkLabel(master=canvas, text='Number Of Constraints')
constLabel.place(x=180, y=50)
entry = customtkinter.CTkEntry(master=canvas, textvariable=numberOfConstraints)
entry.pack(padx=20, pady=50)

typeOfProblem = customtkinter.StringVar(value="Maximization")


def combobox_callback(choice):
    typeOfProblem = choice


combobox = customtkinter.CTkComboBox(master=canvas, values=["Maximization", "Minimization"], command=combobox_callback,
                                     variable=typeOfProblem).pack(padx=20, pady=10)
typeProblemLabel = customtkinter.CTkLabel(master=canvas, text='Type of Problem')
typeProblemLabel.place(x=180, y=140)


def main_function():
    if not numberOfConstraints.get():
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

    top = customtkinter.CTkToplevel()
    top.geometry('800x600')
    top.title('Enter The Data')
    top.iconbitmap('res/form.ico')
    top.resizable(False, False)

    l = customtkinter.CTkLabel(master=top, text='Objective Function')
    l.grid(row=0, column=0, padx=50, pady=10)
    e = customtkinter.CTkEntry(master=top, width=220)
    e.grid(row=0, column=1, padx=10, pady=10)

    for j in range(intConstraints):
        enumeratedLabel = customtkinter.CTkLabel(master=top, text='Constraint: ' + str(j + 1))
        enumeratedLabel.grid(row=j + 1, column=0, padx=10)

        enumeratedEntry = customtkinter.CTkEntry(master=top, width=220)
        enumeratedEntry.grid(row=j + 1, column=1, padx=10, pady=10)

    customtkinter.CTkButton(master=top, text='Confirm', corner_radius=8,
                            command=main_function, font=('SAN_SERIF', 15, 'bold')).place(x=300, y=300)


customtkinter.CTkButton(master=canvas, text='Confirm', corner_radius=8,
                        command=main_function, font=('SAN_SERIF', 15, 'bold')).place(x=300, y=300)

canvas.mainloop()
