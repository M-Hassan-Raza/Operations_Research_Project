from tkinter import *
from tkinter import messagebox
from pulp import *

import customtkinter

#
canvas = customtkinter.CTk()
canvas.geometry('800x600')
canvas.title('Linear Programming Solver')
canvas.iconbitmap('res/line-chart.ico')
canvas.resizable(False, False)
customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("light")

canvas_open = True
entry_form_open = False
final_window_open = False

numberOfConstraints = 0
nameOfProblem = 'Giapetto'
listOfConstraints = []
listOfDecisionVariables = []
listOfFormattedDecisionVariables = []
lowerBound = 0
objectiveFunction = '20*x1 + 30*x2'
listOfReferences = []
constraintNumber = 0

# menubar = Menu(canvas)
# canvas.config(menu=menubar)
# about_menu =
# about_menu.add_command(label='About', command=show_about_menu)

constLabel = customtkinter.CTkLabel(master=canvas, text='Name of The Problem')
constLabel.place(x=180, y=30)
entry = customtkinter.CTkEntry(master=canvas, textvariable=nameOfProblem)
entry.pack(padx=20, pady=30)

constLabel = customtkinter.CTkLabel(master=canvas, text='Number Of Constraints')
constLabel.place(x=180, y=120)
entry = customtkinter.CTkEntry(master=canvas, textvariable=numberOfConstraints)
entry.pack(padx=20, pady=30)

typeOfProblem = customtkinter.StringVar(value="Maximization")


def combobox_callback(choice):
    typeOfProblem = choice


combobox = customtkinter.CTkComboBox(master=canvas, values=["Maximization", "Minimization"], command=combobox_callback,
                                     variable=typeOfProblem).pack(padx=20, pady=10)
typeProblemLabel = customtkinter.CTkLabel(master=canvas, text='Type of Problem')
typeProblemLabel.place(x=180, y=190)


def go_back():
    canvas.iconify()


def solve_problem():
    finalWindow = customtkinter.CTkToplevel()
    finalWindow.geometry('900x900')
    finalWindow.title('Results')
    finalWindow.iconbitmap('res/results.ico')
    finalWindow.resizable(True, True)

    if typeOfProblem == 'Maximize':
        problem = LpProblem(str(nameOfProblem), LpMaximize)
    else:
        problem = LpProblem(str(nameOfProblem), LpMinimize)

    for x in range(constraintNumber):
        listOfConstraints[x] = listOfReferences[x].get()

    for y in range(constraintNumber):
        listOfFormattedDecisionVariables[y] = LpVariable(str(listOfDecisionVariables[y]), lowBound=lowerBound)

    problem += objectiveFunction

    for i in range(constraintNumber):
        problem += listOfConstraints[i]

    print(problem)


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
            constraintNumber = intConstraints
        except ValueError:
            messagebox.showinfo('Error', 'Number of constraints must be an integer value')
            return

    canvas.withdraw()
    top = customtkinter.CTkToplevel()
    top.geometry('900x900')
    top.title('Enter The Data')
    top.iconbitmap('res/form.ico')
    top.resizable(True, True)

    labelLooped = customtkinter.CTkLabel(master=top, text='Objective Function')
    labelLooped.grid(row=0, column=0, padx=80, pady=10)
    entryLooped = customtkinter.CTkEntry(master=top, width=220)
    entryLooped.grid(row=0, column=1, padx=10, pady=10)

    for j in range(intConstraints):
        enumeratedLabel = customtkinter.CTkLabel(master=top, text='Constraint: ' + str(j + 1))
        enumeratedLabel.grid(row=j + 1, column=0, padx=10)

        enumeratedEntry = customtkinter.CTkEntry(master=top, width=220)
        enumeratedEntry.grid(row=j + 1, column=1, padx=10, pady=10)

        listOfDecisionVariables.append(str('x' + str(j + 1)))
        listOfReferences.append(enumeratedEntry)

    lowerBoundLabel = customtkinter.CTkLabel(master=top, text='All Xs >= ')
    lowerBoundLabel.grid(row=intConstraints + 2, column=0, padx=10)

    lowerBoundEntry = customtkinter.CTkEntry(master=top, width=220)
    lowerBoundEntry.grid(row=intConstraints + 2, column=1, padx=10, pady=10)

    prev_button = customtkinter.CTkButton(master=top, text='←', command=go_back, width=32, height=32, corner_radius=100)
    prev_button.place(x=10, y=10)

    solve_button = customtkinter.CTkButton(master=top, text='Solve', corner_radius=8,command=solve_problem, font=('SAN_SERIF', 25, 'bold'))
    solve_button.place(x=320, y=520)



customtkinter.CTkButton(master=canvas, text='Confirm', corner_radius=8, command=main_function, font=('SAN_SERIF', 30, 'bold')).place(x=320, y=420)

canvas.mainloop()
