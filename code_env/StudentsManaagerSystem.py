
def  addstudent():
    def submitadd():
        pass
        
    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry("470x470+220+200")
    addroot.title("Student Managements System")
    addroot.config(bg='blue')
    addroot.iconbitmap('Mana.ico')
    addroot.resizable(False,False)
    #--------------- add student labal
    idlabal =Label(addroot,text='ID:',bg = "gold",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabal.place(x= 10,y =10)#1
    namelabal =Label(addroot,text='Name:',bg = "gold",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabal.place(x= 10,y =70)#2
    mobilelabal =Label(addroot,text='Mobile:',bg = "gold",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabal.place(x= 10,y =130)#3
    emaillabal =Label(addroot,text='Email:',bg = "gold",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabal.place(x= 10,y =190)#4
    addresslabal =Label(addroot,text='Address:',bg = "gold",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabal.place(x= 10,y =250)#5
    genderlabal =Label(addroot,text='Gender:',bg = "gold",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabal.place(x= 10,y =310)#6
    doblabal =Label(addroot,text='D.O.B:',bg = "gold",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabal.place(x= 10,y =370)
    #---------------------Add student Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval= StringVar()
    genderval = StringVar()
    dobval = StringVar()
    identry = Entry(addroot,font=('roman',15, 'bold'),bd=5, textvariable= idval)
    identry.place(x = 250, y= 10)#1
    nameentry = Entry(addroot,font=('roman',15, 'bold'),bd=5, textvariable= nameval)
    nameentry.place(x = 250, y= 70)#2
    mobileentry = Entry(addroot,font=('roman',15, 'bold'),bd=5, textvariable= mobileval)
    mobileentry.place(x = 250, y= 130)#3
    emailentry = Entry(addroot,font=('roman',15, 'bold'),bd=5, textvariable= emailval)
    emailentry.place(x = 250, y= 190)#4
    addressentry = Entry(addroot,font=('roman',15, 'bold'),bd=5, textvariable= addressval)
    addressentry.place(x = 250, y= 250)#5
    genderentry = Entry(addroot,font=('roman',15, 'bold'),bd=5, textvariable= genderval)
    genderentry.place(x = 250, y= 310)#6
    dobentry = Entry(addroot,font=('roman',15, 'bold'),bd=5, textvariable= dobval)
    dobentry.place(x = 250, y= 370)#7
    #-----------------add bottom
    submitbt = Button(addroot,text="Submit",font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                      bg='red',command= submitadd)
    submitbt.place(x=150,y = 420)
    
    addroot.mainloop()
def searchstudent():
    def search():
        pass
        
    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry("470x470+220+200")
    searchroot.title("Student Managements System")
    searchroot.config(bg='green')
    searchroot.iconbitmap('Mana.ico')
    searchroot.resizable(False,False)
    #--------------- add student labal
    idlabal =Label(searchroot,text='ID:',bg = "gold",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabal.place(x= 10,y =10)#1
    namelabal =Label(searchroot,text='Name:',bg = "gold",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabal.place(x= 10,y =60)#2
    mobilelabal =Label(searchroot,text='Mobile:',bg = "gold",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabal.place(x= 10,y =110)#3
    emaillabal =Label(searchroot,text='Email:',bg = "gold",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabal.place(x= 10,y =160)#4
    addresslabal =Label(searchroot,text='Address:',bg = "gold",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabal.place(x= 10,y =210)#5
    genderlabal =Label(searchroot,text='Gender:',bg = "gold",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabal.place(x= 10,y =260)#6
    doblabal =Label(searchroot,text='D.O.B:',bg = "gold",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabal.place(x= 10,y =310)
    datelabal =Label(searchroot,text='DATE:',bg = "gold",font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabal.place(x= 10,y =360)
    #---------------------Add student Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval= StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar
    identry = Entry(searchroot,font=('roman',15, 'bold'),bd=5, textvariable= idval)
    identry.place(x = 250, y= 10)#1
    nameentry = Entry(searchroot,font=('roman',15, 'bold'),bd=5, textvariable= nameval)
    nameentry.place(x = 250, y= 60)#2
    mobileentry = Entry(searchroot,font=('roman',15, 'bold'),bd=5, textvariable= mobileval)
    mobileentry.place(x = 250, y= 110)#3
    emailentry = Entry(searchroot,font=('roman',15, 'bold'),bd=5, textvariable= emailval)
    emailentry.place(x = 250, y= 160)#4
    addressentry = Entry(searchroot,font=('roman',15, 'bold'),bd=5, textvariable= addressval)
    addressentry.place(x = 250, y= 210)#5
    genderentry = Entry(searchroot,font=('roman',15, 'bold'),bd=5, textvariable= genderval)
    genderentry.place(x = 250, y= 260)#6
    dobentry = Entry(searchroot,font=('roman',15, 'bold'),bd=5, textvariable= dobval)
    dobentry.place(x = 250, y= 310)#7
    dateentry = Entry(searchroot,font=('roman',15, 'bold'),bd=5, textvariable= dateval)
    dateentry.place(x = 250, y= 360)#8
    #-----------------add bottom
    submitbt = Button(searchroot,text="Search",font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                      bg='red',command= search)
    submitbt.place(x=150,y = 410)
    
    searchroot.mainloop()
def deletestudent():
    pass
def updatestudent():
    def search():
        pass
        
    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry("470x470+220+200")
    updateroot.title("Student Managements System")
    updateroot.config(bg='pink')
    updateroot.iconbitmap('Mana.ico')
    updateroot.resizable(False,False)
    #--------------- add student labal
    idlabal =Label(updateroot,text='ID:',bg = "gold",font=('times',17,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabal.place(x= 10,y =10)#1
    namelabal =Label(updateroot,text='Name:',bg = "gold",font=('times',17,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabal.place(x= 10,y =50)#2
    mobilelabal =Label(updateroot,text='Mobile:',bg = "gold",font=('times',17,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabal.place(x= 10,y =90)#3
    emaillabal =Label(updateroot,text='Email:',bg = "gold",font=('times',17,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabal.place(x= 10,y =130)#4
    addresslabal =Label(updateroot,text='Address:',bg = "gold",font=('times',17,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabal.place(x= 10,y =170)#5
    genderlabal =Label(updateroot,text='Gender:',bg = "gold",font=('times',17,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabal.place(x= 10,y =210)#6
    doblabal =Label(updateroot,text='D.O.B:',bg = "gold",font=('times',17,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabal.place(x= 10,y =250)#7
    datelabal =Label(updateroot,text='DATE:',bg = "gold",font=('times',17,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabal.place(x= 10,y =290)#8
    timelabal =Label(updateroot,text='DATE:',bg = "gold",font=('times',17,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    timelabal.place(x= 10,y =330)#9
    #---------------------Add student Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval= StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar
    timeval = StringVar
    identry = Entry(updateroot,font=('roman',15, 'bold'),bd=5, textvariable= idval)
    identry.place(x = 250, y= 10)#1
    nameentry = Entry(updateroot,font=('roman',15, 'bold'),bd=5, textvariable= nameval)
    nameentry.place(x = 250, y= 50)#2
    mobileentry = Entry(updateroot,font=('roman',15, 'bold'),bd=5, textvariable= mobileval)
    mobileentry.place(x = 250, y= 90)#3
    emailentry = Entry(updateroot,font=('roman',15, 'bold'),bd=5, textvariable= emailval)
    emailentry.place(x = 250, y= 130)#4
    addressentry = Entry(updateroot,font=('roman',15, 'bold'),bd=5, textvariable= addressval)
    addressentry.place(x = 250, y= 170)#5
    genderentry = Entry(updateroot,font=('roman',15, 'bold'),bd=5, textvariable= genderval)
    genderentry.place(x = 250, y= 210)#6
    dobentry = Entry(updateroot,font=('roman',15, 'bold'),bd=5, textvariable= dobval)
    dobentry.place(x = 250, y= 240)#7
    dateentry = Entry(updateroot,font=('roman',15, 'bold'),bd=5, textvariable= dateval)
    dateentry.place(x = 250, y= 290)#8
    timeentry = Entry(updateroot,font=('roman',15, 'bold'),bd=5, textvariable= timeval)
    timeentry.place(x = 250, y= 330)#9
    #-----------------add bottom
    submitbt = Button(updateroot,text="Search",font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',
                      bg='red',command= search)
    submitbt.place(x=150,y = 380)
    
    updateroot.mainloop()
def showstudent():
    pass
def exportstudent():
    pass
def exit():
    res = messagebox.askokcancel('notification','do you want to exit')   
    if (res == True):
        root.destroy()
    
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

colors = ["white"]
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
from tkinter import Toplevel,messagebox
import time
import random
from tkinter import font
root = Tk()
root.title(" Students Managements System ")
root.config(bg='blue')
root.geometry("1174x700+200+50")
root.iconbitmap('Mana.ico')
root.resizable(False,False)
########################## Frame
DataEntryFrame = Frame(root,bg='white',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x= 10,y=80, width=500, height=600)
#_--------------------------------------dataentry farme intro
forntlabal = Label(DataEntryFrame,text = "---------Welcome---------",width=30,font = ("arial",22,'italic bold'),bg = 'gold' )
forntlabal.pack(side= TOP,expand= True)
#------------------- show data frame
addbutton = Button(DataEntryFrame, text= "1. Add Student",width= 25, font=("chiller",20,'bold'),bd = 6,bg= 'skyblue',activebackground='blue',relief=RIDGE,
                   activeforeground= 'white',command= addstudent)
addbutton.pack(side=TOP,expand= True)#1
searchbutton = Button(DataEntryFrame, text= "2. Search Student",width= 25, font=("chiller",20,'bold'),bd = 6,bg= 'skyblue',activebackground='blue',relief=RIDGE,
                   activeforeground= 'white',command= searchstudent)
searchbutton.pack(side=TOP,expand= True)#2
deletebutton = Button(DataEntryFrame, text= "3. delete Student",width= 25, font=("chiller",20,'bold'),bd = 6,bg= 'skyblue',activebackground='blue',relief=RIDGE,
                   activeforeground= 'white',command= deletestudent)
deletebutton.pack(side=TOP,expand= True)#3
updatebutton = Button(DataEntryFrame, text= "4. Update Student",width= 25, font=("chiller",20,'bold'),bd = 6,bg= 'skyblue',activebackground='blue',relief=RIDGE,
                   activeforeground= 'white',command= updatestudent)
updatebutton.pack(side=TOP,expand= True)#4
showbutton = Button(DataEntryFrame, text= "5.  Show ALL",width= 25, font=("chiller",20,'bold'),bd = 6,bg= 'skyblue',activebackground='blue',relief=RIDGE,
                   activeforeground= 'white',command= showstudent)
showbutton.pack(side=TOP,expand= True)#5
exportbutton = Button(DataEntryFrame, text= "6.  Export data",width= 25, font=("chiller",20,'bold'),bd = 6,bg= 'skyblue',activebackground='blue',relief=RIDGE,
                   activeforeground= 'white',command= exportstudent)
exportbutton.pack(side=TOP,expand= True)#6
exitbutton = Button(DataEntryFrame, text= "7. Exit",width= 25, font=("chiller",20,'bold'),bd = 6,bg= 'skyblue',activebackground='blue',relief=RIDGE,
                   activeforeground= 'white',command= exit)
exitbutton.pack(side=TOP,expand= True)#7


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