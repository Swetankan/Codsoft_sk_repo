#task -2 Calculator by Swetankan Kumar Sinha (Batch-A28)

#importing Tkinter Library
from tkinter import *

#creating root
calc_root=Tk()
calc_root.title("CALCULATOR")
#calc_root.title("CALCULATOR")
calc_root.geometry("364x490+1100+150")
calc_root.resizable(FALSE,FALSE)

#function defination for the calculation
def calculate(no):
    global display
    display=display+str(no)
    output.set(display)

#function to clear display
def clear():
    global display
    display=""
    output.set("")

#function to calculate results
def equal():
    global no
    global display
    #exception halding
    try:
        no=eval(display)
        display=str(no)
        output.set(display)
    except ZeroDivisionError:
        output.set("Zero Division Error")
    except Exception as e:
        if display=="":
            output.set("")  
        else:
            output.set("Invalid Input")
        
#variable declarations
no=""
display=""

#Entry point to take input and display results
output=StringVar()
disp=Entry(calc_root,bd=20, bg="#84a494", font="Candra 21", fg="black", justify="right", textvariable=output)    
disp.place(width=362, height=100, x=0, y=0) 


#buttons

#row-1
Button(calc_root, font="Candra 20", bg="red",   fg="white",      bd=10, height=1, width=4, text="C",command=lambda : clear()).place(x=0, y=105)
Button(calc_root, font="Candra 20", bg="white", fg="light green",bd=10, height=1, width=4, text="%",command=lambda : calculate("%")).place(x=91, y=105)
Button(calc_root, font="Candra 20", bg="white", fg="light green",bd=10, height=1, width=4, text="÷",command=lambda : calculate("/")).place(x=182, y=105)
Button(calc_root, font="Candra 20", bg="white", fg="light green",bd=10, height=1, width=4, text="x",command=lambda : calculate("*")).place(x=273, y=105)

#row-2
Button(calc_root, font="Candra 20", bg="white", fg="black",      bd=10, height=1, width=4, text="7",command=lambda : calculate(7)).place(x=0, y=178)
Button(calc_root, font="Candra 20", bg="white", fg="black",      bd=10, height=1, width=4, text="8",command=lambda : calculate(8)).place(x=91, y=178)
Button(calc_root, font="Candra 20", bg="white", fg="black",      bd=10, height=1, width=4, text="9",command=lambda : calculate(9)).place(x=182, y=178)
Button(calc_root, font="Candra 20", bg="white", fg="light green",bd=10, height=1, width=4, text="+",command=lambda : calculate("+")).place(x=273, y=178)

#row-3
Button(calc_root, font="Candra 20", bg="white", fg="black",      bd=10, height=1, width=4, text="4",command=lambda : calculate(4)).place(x=0, y=251)
Button(calc_root, font="Candra 20", bg="white", fg="black",      bd=10, height=1, width=4, text="5",command=lambda : calculate(5)).place(x=91, y=251)
Button(calc_root, font="Candra 20", bg="white", fg="black",      bd=10, height=1, width=4, text="6",command=lambda : calculate(6)).place(x=182, y=251)
Button(calc_root, font="Candra 20", bg="white", fg="light green",bd=10, height=1, width=4, text="-",command=lambda : calculate("-")).place(x=273, y=251)

#row-4
Button(calc_root, font="Candra 20", bg="white", fg="black",      bd=10, height=1, width=4, text="1",command=lambda : calculate(1)).place(x=0, y=324)
Button(calc_root, font="Candra 20", bg="white", fg="black",      bd=10, height=1, width=4, text="2",command=lambda : calculate(2)).place(x=91, y=324)
Button(calc_root, font="Candra 20", bg="white", fg="black",      bd=10, height=1, width=4, text="3",command=lambda : calculate(3)).place(x=182, y=324)
Button(calc_root, font="Candra 20", bg="blue",  fg="white",      bd=10, height=1, width=4, text="=",command=lambda : equal()).place(height=145, width=90,x=273, y=324)

#row-5
Button(calc_root, font="Candra 20", bg="white", fg="black",      bd=10, height=1, width=4, text="0",command=lambda : calculate(0)).place(height=72, width=180,x=0, y=397)
Button(calc_root, font="Candra 20", bg="white", fg="black",      bd=10, height=1, width=4, text=".",command=lambda : calculate(".")).place(x=182, y=397)

Label(calc_root, font="FZShuti  8 bold",fg="black", text="#Devloped by Swetankan").place(x=212,y=470)
calc_root.mainloop()
