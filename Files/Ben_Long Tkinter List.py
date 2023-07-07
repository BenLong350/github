#Tkinter

from tkinter import *

root = Tk()

labels = [Label(root, text="This is a Grocery List", height= 7, width= 52, bg= "grey", fg= "blue"), Label(root, text="Iteam1:", height= 3, width= 52, bg= "grey", fg= "blue"), Label(root, text="Iteam2:", height= 3, width= 52, bg= "grey", fg= "blue"), Label(root, text="Iteam3:", height= 3, width= 52, bg= "grey", fg= "blue"), Label(root, text="Iteam4:", height= 3, width= 52, bg= "grey", fg= "blue"), Label(root, text="Iteam5:", height= 3, width= 52, bg= "grey", fg= "blue")]
entries = [Entry(root), Entry(root), Entry(root), Entry(root), Entry(root)]
for label, entry in zip(labels, entries):
    label.pack()
    entry.pack()

def command():
    print([entry.get() for entry in entries])

Button(root, text="print", command=command).pack()

root.mainloop()