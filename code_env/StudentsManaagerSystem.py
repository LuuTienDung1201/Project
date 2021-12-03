
def Connectdb():
    dbroot = Toplevel()
    dbroot.geometry('470x250+800+230')
    dbroot.grab_set()
    dbroot.iconbitmap("mana.ico")
    dbroot.resizable(False,False)
    dbroot.config(bg="blue")
    #-------------------------connectdb lables
    hostLabel = Label(dbroot,text="Enter host: ",bg = "red",\
        font= ("times",20,'bold'),relief= GROOVE,borderwidth=3,width=13,anchor="w")
    hostLabel.place(x = 10,y =10)
    
    userLabel = Label(dbroot,text="Enter user: ",bg = "red",\
        font= ("times",20,'bold'),relief= GROOVE,borderwidth=3,width=13,anchor="w")
    userLabel.place(x = 10,y =70)
    
    passwordLabel = Label(dbroot,text="Enter password: ",bg = "red",\
        font= ("times",20,'bold'),relief= GROOVE,borderwidth=3,width=13,anchor="w")
    passwordLabel.place(x = 10,y =130)
    #--------------------connectdb entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()
    hostentry = Entry(dbroot,font=('roman',15,'bold'),bd =5,textvariable=hostval)
    hostentry.place(x = 250, y =10)
    userentry = Entry(dbroot,font=('roman',15,'bold'),bd =5,textvariable=userval)
    userentry.place(x = 250, y =70)
    passentry = Entry(dbroot,font=('roman',15,'bold'),bd =5,textvariable=passwordval)
    passentry.place(x = 250, y =130)
    #-------------------------
    submitbutton = Button(dbroot,text="Submit",font=("roman",15,'bold'),width= 20,\
        activebackground='blue',activeforeground='white')
    submitbutton.place(x =150,y= 190)
    
    dbroot.mainloop()
def tick():
    time_string= time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string +"\n" +"Time:"+time_string)
    clock.after(20,tick)

colors = ["white","green","blue","yellow","olive","blue2"]
def IntroLabalcolor():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(20,IntroLabalcolor)
def IntrolabelTick():
    global count,text
    if (count >= len(title)):
        count = -1
        text = ''
        SliderLabel.config(text= text)
    else:
        text = text+title[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(210,IntrolabelTick)
####
from  tkinter import *
from tkinter import Toplevel
import time
import random
root = Tk()
root.title(" Students Managements System ")
root.config(bg='blue')
root.geometry("1174x700+200+50")
root.iconbitmap('Mana.ico')
root.resizable(False,False)
########################## Frame
DataEntryFrame = Frame(root,bg='white',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x= 10,y=80, width=500, height=600)

ShowDataFrame =  Frame(root,bg='white',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550, y= 80,width=620,height=600)
########################## Slider
title = 'Students Managements Systems'
count = 0
text = ""
SliderLabel = Label(root,text=title,font=('time new roman',30,'italic bold'),relief=RIDGE,borderwidth=4,width= 27,bg="red")
SliderLabel.place(x=260, y = 0)
IntrolabelTick()
IntroLabalcolor()
clock = Label(root,font=('time',14,'bold'),relief=RIDGE,borderwidth=4,bg="lawn green")
clock.place(x=0,y=0)
tick()

connectbutton = Button(root,text="Connect To DataBase",width=23,font=('time new roman',13,'italic bold'),relief=RIDGE,borderwidth=4,bg="lime",\
    bd=6,activebackground="black",activeforeground="white",command= Connectdb)
connectbutton.place(x = 930, y = 0)
root.mainloop()