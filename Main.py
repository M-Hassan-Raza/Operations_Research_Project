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

numberOfConstraints = StringVar()
nameOfProblem = StringVar()
intConstraints = 0
typeOfProblem = StringVar()
listOfConstraints = []
listOfDecisionVariables = []
listOfFormattedDecisionVariables = []
lowerBound = 0
nameOfProblem = StringVar()
objectiveFunction = StringVar()
problem = StringVar()
listOfReferences = []

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

    canvas.withdraw()
    # if(canvas_open == True):
    #     top.iconify()

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

        listOfDecisionVariables[j] = 'X' + str(j+1)
        listOfReferences.append(enumeratedEntry)

    lowerBoundLabel = customtkinter.CTkLabel(master=top, text='All Xs >= ')
    lowerBoundLabel.grid(row=intConstraints + 2, column=0, padx=10)

    lowerBoundEntry = customtkinter.CTkEntry(master=top, width=220)
    lowerBoundEntry.grid(row=intConstraints + 2, column=1, padx=10, pady=10)

    def solve_problem():
        top.withdraw()
        finalWindow = customtkinter.CTkToplevel()
        finalWindow.geometry('900x900')
        finalWindow.title('Enter The Data')
        finalWindow.iconbitmap('res/form.ico')
        finalWindow.resizable(True, True)

    def go_back():
        top.withdraw()
        canvas.iconify()
        pass

    def confirm_constraints():
        for x in range(intConstraints):
            listOfConstraints[x] = listOfReferences[x].get()

        if(typeOfProblem == 'Maximize'):
            problem = LpProblem(nameOfProblem, LpMaximize)
        else:
            problem = LpProblem(nameOfProblem, LpMinimize)

        for y in range(intConstraints):
            listOfFormattedDecisionVariables[y] = LpVariable(str(listOfDecisionVariables[y]), lowBound=lowerBound)

        solve_problem()

    customtkinter.CTkButton(master=top, text='Confirm Constraints', corner_radius=8,
                            command=confirm_constraints, font=('SAN_SERIF', 15, 'bold')).place(x=320, y=520)

    prev_button = customtkinter.CTkButton(master=top, text='←', command=go_back, width=32, height=32, corner_radius=100)
    prev_button.place(x=10, y=10)


customtkinter.CTkButton(master=canvas, text='Confirm', corner_radius=8,
                        command=main_function, font=('SAN_SERIF', 15, 'bold')).place(x=320, y=420)

canvas.mainloop()
