
from tkinter import *
from tkinter.ttk import Combobox
import tkinter.filedialog as tkFileDialog
from PIL import Image




encode1()
def encode2():
    window = Tk()
    window.title("Encode")
    window.geometry("400x400")

    labelPin = Label(window, text = "Pin: ", font = ("Times New Roman",15))
    labelPin.grid(column = 0, row = 0)
    #1
    label1 = Label(window, text = "Pin 1: ", font = ("Times New Roman",15))
    label1.grid(column = 0, row = 5)

    def clicked1():
        filename1 = tkFileDialog.askopenfilename(parent=window, title='Open file to encrypt')
        img1 = Image.open(filename1)
        print(filename1)

    btn1 = Button(window, text = "Choose File", font = ("Times New Roman", 10), command = clicked1, width = 15)
    btn1.grid(column = 6, row = 5)
    #2
    label2 = Label(window, text="Pin 2: ", font=("Times New Roman", 15))
    label2.grid(column=0, row=10)

    def clicked2():
        filename2 = tkFileDialog.askopenfilename(parent=window, title='Open file to encrypt')
        img2 = Image.open(filename2)
        print(filename2)

    btn2 = Button(window, text="Choose File", font=("Times New Roman", 10), command=clicked2, width=15)
    btn2.grid(column=6, row=10)

    #3

    label3 = Label(window, text="Pin 3: ", font=("Times New Roman", 15))
    label3.grid(column=0, row=15)

    def clicked3():
        filename3 = tkFileDialog.askopenfilename(parent=window, title='Open file to encrypt')
        img3 = Image.open(filename3)
        print(filename3)

    btn3 = Button(window, text="Choose File", font=("Times New Roman", 10), command=clicked3, width=15)
    btn3.grid(column=6, row=15)
    #4

    label4 = Label(window, text="Pin 4: ", font=("Times New Roman", 15))
    label4.grid(column=0, row=20)

    def clicked4():
        filename4 = tkFileDialog.askopenfilename(parent=window, title='Open file to encrypt')
        img4 = Image.open(filename4)
        print(filename4)

    btn4 = Button(window, text="Choose File", font=("Times New Roman", 10), command=clicked4, width=15)
    btn4.grid(column=6, row=20)
    window.mainloop()

encode2()

def decode():
    window = Tk()
    window.title("Decode")
    window.geometry("400x400")

    label = Label(window, text = "")
    label.grid(column = 0, row = 0)

    labelUpload = Label(window, text = "Upload Image here: ", font=("Times New Roman", 15))
    labelUpload.grid(column = 0, row = 5)

    def clicked():
        filename = tkFileDialog.askopenfilename(parent=window, title='Open file to encrypt')
        img4 = Image.open(filename)
        print(filename)

    btn = Button(window, text = "Choose File",font=("Times New Roman", 10), command=clicked, width=15)
    btn.grid (column = 6, row = 5)

    labelPin = Label (window, text = "Pin: ", font=("Times New Roman", 15))
    labelPin.grid(column = 0, row = 10)

    window.mainloop()

decode()