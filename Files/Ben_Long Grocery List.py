#Grocery List


from tkinter import *

root = Tk(className="Grocery List")

a = Label(root, text="My Grocery List", height=6, width=50, bg="blue", fg="grey")
a.config(font = ("Courier", 20))

label = [Label(root, text="Input Grocery:")]
entry = [Entry(root)]
for label, entry in zip(label, entry):
    label.grid()
    entry.grid()

Main_List=["Bread", "Milk", "Apples"]

def update():
    global Main_List
    r = 0
    for c in Main_List:
        Label(text=c, relief=RIDGE,width=15).grid(row=r,column=0)
    
def adding2list() :
    Main_List.append(name)
    a=len(Main_List)
    name.set(a)
    print (Main_List)

num = StringVar()
y = Entry(root, textvariable= num)
y.grid(row=1, column=0)
y.get()

name = StringVar()
b = entry(root)
b.get()
z = Button(root, text="Update", command=update).grid(row=0, column=2)
adding2list = Button(root, text="Add", command=adding2list).grid(row=1, column=1)

print(name)

root.mainloop()