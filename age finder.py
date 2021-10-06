from tkinter import *
from tkinter import ttk
import datetime
#****************** window************
win=Tk()
win.geometry('400x200')
win.title("Age finder")
win.resizable(0,0)
win.configure(bd=4)
#**************************************

def findday():
    d=dv.get()
    m=mv.get()
    y=int(yv.get())
    mc=[0,3,3,6,1,4,6,2,5,0,3,5]
    yc=[6,4,2,4,2,0,6,4,2,0]
    w=["            Sunday","            Monday","            Tuesday","            Wednesday","            Thursday","            Friday","            Saturday"]
    a=str(y)
    l=int(a[1])
    mm=int(a[2:])
    z=d+mm+(mm//4)+mc[m-1]+yc[l]
    result=z%7
    ans=w[result]
    av.set(ans)
def leapyear():
    y=int(yv.get())
    if((y%4==0 and y%100!=0) or (y%400==0)):
        av.set('         Leap Year')
    else:
        av.set('       Not Leap Year')
def findage():
    tday=datetime.date.today()
    y=int(yv.get())
    m=mv.get()
    if(m<tday.month):
        years=tday.year-y
        months=tday.month-m
        
    else:
        years=((tday.year-1)-y)
        months=((tday.month+12)-m)
    av.set("   {} years {} months ".format(years,months))

#***************combobox***************************
dv=IntVar()
date=ttk.Combobox(win,width=16,textvariable=dv,state='readonly')
dt=[]
for i in range(1,32):
    dt.append(i)
date['values']=dt
date.current(0)
date.grid(row=0,column=1)

mv=IntVar()
date=ttk.Combobox(win,width=16,textvariable=mv,state='readonly')
mo=[]
for i in range(1,13):
    mo.append(i)
date['values']=mo
date.current(0)
date.grid(row=1,column=1)
#************************LABELS****************
l2=Label(win,text="MONTH    : ",font=("arial",10,"bold"),fg="brown").grid(row=1,column=0,pady=10,padx=5)
l1=Label(win,text="DATE       : ",font=("arial",10,"bold"),fg="blue").grid(row=0,column=0,pady=10,padx=5)
l3=Label(win,text="YEAR        : ",font=("arial",10,"bold"),fg="green").grid(row=2,column=0,pady=10,padx=5)
#**********************ENTRY*************************
yv=StringVar()
e1=Entry(win,width=20,textvariable=yv).grid(row=2,column=1)

av=StringVar()
e2=Entry(win,textvariable=av,font=("arial",20,"bold"),relief="solid",bd=1.1,fg="red",bg="light grey").place(height=40,x=30,y=150)
#*****************BUTTON******************************
b1=Button(win,text="FIND DAY",command=findday,bd=5,bg="lightyellow").grid(row=0,column=2,padx=50)
b2=Button(win,text='FIND AGE',command=findage,bd=5,bg="lightyellow").grid(row=1,column=2,padx=50)
b2=Button(win,text='check leap year',command=leapyear,bd=5,bg="lightyellow").grid(row=2,column=2,padx=50)
win.mainloop()