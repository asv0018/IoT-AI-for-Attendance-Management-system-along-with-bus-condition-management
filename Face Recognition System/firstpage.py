#import module from tkinter for UI
from tkinter import *
import webbrowser
import os
from datetime import datetime;
#creating instance of TK
root=Tk()

root.configure(background="white")

#root.geometry("300x300")

def function1():
    
    os.system("python3 dataset_capture.py")
    
def function2():
    
    os.system("python3 training_dataset.py")

def function3():

    os.system('python3 uartoiotfacerec.py')
    

def function5():
    popup_bonus()

    
def function6():

    root.destroy()

def popup_bonus():
    win = Toplevel()
    win.wm_title("TEAM MEMBERS")

    l = Label(win, text="A project by ASV.")
    l.grid(row=0, column=0)

    b = Button(win, text="CLOSE", command=win.destroy)
    b.grid(row=1, column=1)
def attend():
    #os.startfile(os.getcwd()+"/firebase/attendance_files/attendance"+str(datetime.now().date())+'.xls')
    webbrowser.open('http://aishwarya.thinkfinitylabs.com/index.php',new=0)
#stting title for the window
root.title("SCHOOL BUS ATTENDANCE USING FACE RECOGNITION")

#creating a text label
Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Create Dataset",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Train Dataset",font=("times new roman",20),bg="#0D47A1",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
Button(root,text="Recognize + Attendance + Bus Health Monitoring",font=('times new roman',20),bg="#0D47A1",fg="white",command=function3).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating attendance button
Button(root,text="View Attendance in Dashboard",font=('times new roman',20),bg="#0D47A1",fg="white",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Project credits",font=('times new roman',20),bg="#0D47A1",fg="white",command=function5).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',20),bg="maroon",fg="white",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
