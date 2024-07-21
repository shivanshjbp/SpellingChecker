from textblob import TextBlob
from tkinter import *

def correct_spelling():
    get_data = enter1.get()
    corr = TextBlob(get_data)
    data = corr.correct()
    enter2.delete(0, END)
    enter2.insert(0, data)

def main_window():
    global enter1, enter2
    win = Tk()
    win.geometry("500x370")
    win.resizable(False, False)
    win.config(bg="#282c34")  
    win.title("Spelling Corrector")

    label1 = Label(win, text="Input Text", font=("Arial", 20, "bold"), bg="#282c34", fg="#61dafb")
    label1.place(x=100, y=20, height=50, width=300)
    
    enter1 = Entry(win, font=("Arial", 18), bg="#abb2bf", fg="#282c34")
    enter1.place(x=100, y=80, height=50, width=300)
    
    label2 = Label(win, text="Corrected Text", font=("Arial", 20, "bold"), bg="#282c34", fg="#61dafb")
    label2.place(x=100, y=140, height=50, width=300)
    
    enter2 = Entry(win, font=("Arial", 18), bg="#abb2bf", fg="#282c34")
    enter2.place(x=100, y=200, height=50, width=300)
    
    button = Button(win, text="Correct", font=("Arial", 18, "bold"), bg="#61dafb", fg="#282c34", command=correct_spelling)
    button.place(x=150, y=280, height=50, width=200)

    win.mainloop()

main_window()
