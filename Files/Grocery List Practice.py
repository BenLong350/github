Main_Q =["read","clean dishes", "wash car"]


from tkinter import*
root=Tk(className="total tasks in the Q")


#formula

def update():
    global Main_Q
    a=len(Main_Q)
    num.set(a)

def add2list():
    Main_Q.append(name)
    a=len(Main_Q)
    num.set(a)
    print (Main_Q)


#output

num=StringVar()
y=Label(root, textvariable=num).grid(row=0, column=1)

#input

name=StringVar()
b=Entry(root, textvariable=name).grid(row=7,column=0)


#buttons
z=Button(root, text="update", command=update).grid(row=7, column=2)
add2list=Button(root,text="add", command=add2list).grid(row=7,         
column=1)


r = 0
for c in Main_Q:
    Label(text=c, relief=RIDGE,width=15).grid(row=r,column=0)
r = r + 1

root.mainloop()