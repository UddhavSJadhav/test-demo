from tkinter import *
import tkinter as tk
import random
from tkinter import messagebox

root = tk.Tk()
root.geometry("450x250+500+300")
root.title("PyMathGame!")

welcomeLabel = tk.Label(text="PyMathGame").pack()
startLabel = tk.Label(text='Select a math operation to start').pack()

root.counter = 0
root.seconds = 61


def genRandom():
    a = random.randrange(1,10,1)
    b = random.randrange(1,10,1)

    return a, b

def calculate(method):

    global correctAnswer
    global met
    met = method

    ranNumber = genRandom()

    if method == "Add":
        correctAnswer = int(ranNumber[0] + ranNumber[1])
        calcString = "+"
    elif method == "Sub":
        correctAnswer = int(ranNumber[0] - ranNumber[1])
        calcString = "-"
    elif method == "Mul":
        correctAnswer = int(ranNumber[0] * ranNumber[1])
        calcString = "*"
    

    QuestionLbl = tk.Label(text="What does {0} {1} {2} equal?".format(ranNumber[0], calcString, ranNumber[1]))
    QuestionLbl.place(x=0, y=125)

    global answerEntry
    answerEntry = Entry()
    answerEntry.place(x=300, y=125)
    
    isCorrectBtn = tk.Button(text="Check Answer", command=isCorrect)
    isCorrectBtn.place(x=300, y = 150)
    
def isCorrect():
    try:
        answerEntered = int(answerEntry.get())

        if answerEntered != correctAnswer:
            checkAnswerLbl = tk.Label(text="Try again :(               ")
            checkAnswerLbl.place(x=150, y=125)
        elif answerEntered == correctAnswer:
            checkAnswerLbl = tk.Label(text="Correct ;)                 ")
            checkAnswerLbl.place(x=150, y=125)
            root.counter += 1
        calculate(met)
    except:
        checkAnswerLbl = tk.Label(text="Enter valid integer ;)")
        checkAnswerLbl.place(x=150, y=125)

def fun(n):
    calculate(n)
    timer()

def timer():

    if root.seconds > 0:
        root.seconds = root.seconds - 1
        mins = root.seconds // 60
        m = str(mins)
        
        if mins < 10:
            m = '0' + str(mins)
        se = root.seconds - (mins * 60)
        s = str(se)

        if se < 10:
            s = '0' + str(se)
        time.set(m + ':' + s)
        timer_display.config(textvariable=time)
        # call this function again in 1,000 milliseconds
        root.after(1000, timer)

    elif root.seconds == 0:
        messagebox.showinfo('Message', 'Your score is : '+ str(root.counter))
        root.destroy()

time = StringVar()
timer_display = tk.Label(root, font=('Trebuchet MS', 20))
timer_display.place(x=180, y=200)


addBtn = tk.Button(text="Addition", command=lambda: fun("Add"))
addBtn.place(x=160, y = 60)
subBtn = tk.Button(text="Subtraction", command=lambda: fun("Sub"))
subBtn.place(x=220, y=60)
subBtn = tk.Button(text="Multiplication", command=lambda: fun("Mul"))
subBtn.place(x=185, y=90)
#subBtn = tk.Button(text="Division", command=lambda: calculate("Div"))
#subBtn.place(x=250, y=90)


tk.mainloop()
