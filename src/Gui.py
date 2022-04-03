# Nama  : Muhammad Gilang Ramadhan
# NIM   : 13520137
# Gui.py
# 15-Puzzle Solver with Branch and Bound Algorithm

from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import tkinter
import os
import time
from Puzzle import Puzzle
from Puzzle import *
from tkinter.messagebox import showinfo

# Initialate Global Variables

# puzzle solving details
Tempkurang = []
ValuekurangSum = 0
TempX = []
mincost = 0
duration = 0
total = 0

# file input
file = ""

# puzzle animation config default
puzzle_labels=[[0 for i in range(4)] for j in range(4)]
puzzle_start = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
zero_pos = (3,3)
Tempmoves = []

# puzzle labels
def Puzzle_Labels():
    for i in range(4):
        for j in range(4):
            puzzle_labels[i][j] = Label(root, text = str(i*4+j+1), font=('calibre',9),
                height= 1, width=2, anchor=CENTER,
                borderwidth=2, relief="solid", bg='yellow')
            puzzle_labels[i][j].place(x=110+20*j, y=120+20*i)
    puzzle_labels[3][3].config(text= " ")

# call puzzle solver
def Callsolve():
    """ Function to executing the puzzle by call the solve function 
    for solve the problem with Branch and Bound Algorithm """
    global puzzle_start, zero_pos, moves, puzzle_labels
    global Tempkurang, ValuekurangSum, X, mincost, duration, total

    visualize_button.place_forget()
    reset_button.place_forget()

    if (len(file) != 0):
        psolver = Puzzle(file)
        if (len(psolver.puzzle)!=0):
            showinfo('Solution', 'Please Wait...')
            root.update()
            # CALL FUCNTION
            start = time.time()
            # Using Branch and Bound Algorithm for solve the puzzle
            ValuekurangSum = psolver.solve()
            end = time.time()
            print('Done')
            duration = end - start
            if (ValuekurangSum%2 == 0):    
                showinfo('Solution', 'The Solution has founded!')
                puzzle_start = copy.deepcopy(psolver.puzzle)
                moves = copy.deepcopy(psolver.Solution)
                visualize_button.place(x=110, y=220)
                reset_button.place(x=185, y=255)
            else:
                showinfo('Solution', 'The puzzle doesnt have solution!')
                puzzle_start = copy.deepcopy(psolver.puzzle)
                moves = []

            Tempkurang = copy.deepcopy(psolver.Tempkurang)
            X = psolver.ValueX
            mincost = psolver.mincost
            total = psolver.total
            details_button.place(x=35, y=255)
            ResetPuzz()
        else:
            showinfo('Solution', 'File config invalid!')
            return
    else:
        showinfo('Solution', 'File config invalid!')
        return

# file select button
def select_file():
    global file
    TypesFile = (('text files', '*.txt'), ('All files', '*.*'))
    name = fd.askopenfilename(title='Open a file', initialdir='./test/input',filetypes=TypesFile)
    filename_label.config(text = "File config: " + os.path.basename(name))
    file = name

# Save File
def saveFile():
    puzzle = puzzle_start
    ZeroPosY = zero_pos[0]
    ZeroPosX = zero_pos[1]
    count = 0
    if (len(moves) > 0):
        f = fd.asksaveasfile(initialfile = 'Untitled.txt', defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        f.write("SOLUTION : \n")
        f.write("\n")
        for dxy in moves:
            count += 1
            f.write(str(count) + " ")
            if (dxy[0] == -1 and dxy[1] == 0):
                f.write("UP\n")
            elif (dxy[0] == 0 and dxy[1] == -1):
                f.write("LEFT\n")
            elif (dxy[0] == 1 and dxy[1] == 0):
                f.write("DOWN\n")
            elif (dxy[0] == 0 and dxy[1] == 1):
                f.write("RIGHT\n")
            f.write("===============================\n")
            # SWAP
            temp = puzzle[ZeroPosY][ZeroPosX]
            puzzle[ZeroPosY][ZeroPosX] = puzzle[dxy[0] + ZeroPosY][dxy[1] + ZeroPosX]
            puzzle[dxy[0] + ZeroPosY][dxy[1] + ZeroPosX] = temp
            for i in range(len(puzzle)):
                for j in range(len(puzzle[i])):
                    f.write(str(puzzle[i][j]) + " ")
                f.write("\n")
            f.write("\n")
            ZeroPosY = dxy[0] + ZeroPosY
            ZeroPosX = dxy[1] + ZeroPosX
    else:
        showinfo('Warning', 'Input is invalid')

# Reset Puzzle
def ResetPuzz():
    global zero_pos
    for i in range(4):
        for j in range(4):
            if puzzle_start[i][j]!=0:
                puzzle_labels[i][j].config(text = str(puzzle_start[i][j])) 
            else:
                zero_pos = (i,j)
                puzzle_labels[i][j].config(text = "")
    root.update()     

# visualize solution
def Visualize():
    global puzzle_labels
    ResetPuzz()
    zero = copy.deepcopy(zero_pos)
    puzzle = copy.deepcopy(puzzle_start)
    for Dxy in moves:
        time.sleep(1)
        dx, dy = Dxy
        zx, zy = zero
        puzzle[zx][zy], puzzle[zx+dx][zy+dy] = puzzle[zx+dx][zy+dy], puzzle[zx][zy]
        puzzle_labels[zx+dx][zy+dy].config(text = "")
        puzzle_labels[zx][zy].config(text = str(puzzle[zx][zy]))
        zero = (zx + dx, zy + dy)
        root.update()

# Details Process
def Details():
    INFO = ">>>>>>KURANG(i)<<<<<<\n"
    for i in range(1,17):
        if (i < 16):
            INFO += "Value KURANG(" + str(i) + ") "  +": " + str(Tempkurang[i]) + "\n"
        else:
            INFO += "Value KURANG(" + str(i) + ") "  +": " + str(Tempkurang[0]) + "\n"
    INFO += "The Numbers of kurang function : " + str(ValuekurangSum) + "\n"
    INFO += "Nodes Generates : " + str(total) + "\n"
    INFO += "Time Execution : "+str(duration*1000)+" ms\n" 
    showinfo(title='Details Solution', message=INFO)

# save button
def saveFile_Button():
    menu = tkinter.Menu(root)
    root.config(menu=menu)
    fileMenu = tkinter.Menu(menu, tearoff=0)
    menu.add_cascade(label='Export Solution', menu=fileMenu)
    fileMenu.add_command(label='Save Puzzle', command=saveFile)

# Gui Setting
def setting_GUI():
    # Title and size
    root.title("15-Puzzle Solver | Gilang")
    root.geometry("300x300")

    # label
    prompt_label.place(x=81, y=7)

    # open button
    open_button.place(x=110, y=29)

    # filename
    filename_label.place(x=75, y=57)

    # Solve button
    solve_button.place(x=110, y=78)

    # Kurang_label
    kurang_label.place(x=20, y=105)

if __name__ == "__main__":
    # Initialate GUI
    root=Tk()
    root.geometry("1000x1000")
    root['background'] = 'green'

    puzzle_labels=[[0 for i in range(4)] for j in range(4)]
    Puzzle_Labels()
    prompt_label = Label(root, text = 'Please input your puzzle :', font=('calibre', 9), bg='green')
    open_button = ttk.Button(root, text='Select file', command=select_file)
    filename_label = Label(root, text = 'File config has not selected', font=('calibre', 9), bg='green')
    solve_button = ttk.Button(root, text='Solve', command=Callsolve)
    kurang_label = Label(root, text = '', font=('calibre',8), bg='green')
    visualize_button = ttk.Button(root, text='Visualize', command=Visualize) 
    reset_button = ttk.Button(root, text='Reset', command=ResetPuzz)
    details_button = ttk.Button(root, text='Details', command=Details)

    setting_GUI()

    saveFile_Button()

    root.mainloop()