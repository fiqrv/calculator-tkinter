#Tutorial exercise based on https://youtu.be/YXPyB4XeYLA
from tkinter import *

root = Tk()
root.title("Casio Fx-570")
root.configure(bg='#53565f')

def funcClr():
    e.delete(0, END)

def funcAdd():
    global fNum
    global oType
    gfNum = e.get()
    oType = "add"
    fNum = int(gfNum)
    e.delete(0, END)

def funcMul():
    global fNum
    global oType
    gfNum = e.get()
    oType = "mul"
    fNum = int(gfNum)
    e.delete(0, END)

def funcDiv():
    global fNum
    global oType
    gfNum = e.get()
    oType = "div"
    fNum = int(gfNum)
    e.delete(0, END)

def funcSubt():
    global fNum
    global oType
    gfNum = e.get()
    oType = "subt"
    fNum = int(gfNum)
    e.delete(0, END)

def funcEqu():
    gsNum = e.get()
    e.delete(0, END)
    if oType == "add":
        e.insert(0, fNum + int(gsNum))
    if oType == "mul":
        e.insert(0, fNum * int(gsNum))
    if oType == "div":
        e.insert(0, int(fNum / int(gsNum)))
    if oType == "subt":
        e.insert(0, fNum - int(gsNum))

def enNum(num):
    cur = e.get()
    e.delete(0, END)
    e.insert(0, str(cur) + str(num))

e = Entry(root, width=33, bg='#53565f', font=('Calibri 20'))
e.grid(row=0, column=0, columnspan=5, padx=5, pady=5, ipady=10)

b7 = Button(root, text="7", padx=40, pady=20, bg='#171a1f', fg='#fdffff', command=lambda: enNum(7))
b8 = Button(root, text="8", padx=40, pady=20, bg='#171a1f', fg='#fdffff', command=lambda: enNum(8))
b9 = Button(root, text="9", padx=40, pady=20, bg='#171a1f', fg='#fdffff', command=lambda: enNum(9))
b4 = Button(root, text="4", padx=40, pady=20, bg='#171a1f', fg='#fdffff', command=lambda: enNum(4))
b5 = Button(root, text="5", padx=40, pady=20, bg='#171a1f', fg='#fdffff', command=lambda: enNum(5))
b6 = Button(root, text="6", padx=40, pady=20, bg='#171a1f', fg='#fdffff', command=lambda: enNum(6))
b1 = Button(root, text="1", padx=40, pady=20, bg='#171a1f', fg='#fdffff', command=lambda: enNum(1))
b2 = Button(root, text="2", padx=40, pady=20, bg='#171a1f', fg='#fdffff', command=lambda: enNum(2))
b3 = Button(root, text="3", padx=40, pady=20, bg='#171a1f', fg='#fdffff', command=lambda: enNum(3))
b0 = Button(root, text="0", padx=40, pady=20, bg='#171a1f', fg='#fdffff', command=lambda: enNum(0))

bClr = Button(root, text="CLR", padx=33, pady=20, bg='#7d8180', fg='#fdffff', command=funcClr)
bMul = Button(root, text="x", padx=40, pady=20, bg='#7d8180', fg='#fdffff', command=funcMul)
bDiv = Button(root, text="÷", padx=40, pady=20, bg='#7d8180', fg='#fdffff', command=funcDiv)
bAdd = Button(root, text="+", padx=40, pady=20, bg='#7d8180', fg='#fdffff', command=funcAdd)
bSubt = Button(root, text="-", padx=40, pady=20, bg='#7d8180', fg='#fdffff', command=funcSubt)
bEqu = Button(root, text="=", padx=40, pady=20, bg='#7d8180', fg='#fdffff', command=funcEqu)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)
bClr.grid(row=1,column=4)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
bMul.grid(row=2,column=3)
bDiv.grid(row=2,column=4)

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
bAdd.grid(row=3,column=3)
bSubt.grid(row=3,column=4)

b0.grid(row=4,column=0)
bEqu.grid(row=4,column=4)

root.mainloop()