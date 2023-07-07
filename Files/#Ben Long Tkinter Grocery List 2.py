#Ben Long Tkinter Grocery List 2

from tkinter import*
from tkinter import ttk 

root = Tk()

root.config(height= 30, width= 700)

a = Label(root, text="Grocery List", height = 4, width= 700)
a.pack()

label = [Label(root, text="Iteam:")]
entry = [Entry(root)]
for label, entry in zip(label, entry):
    label.pack()
    entry.pack()
    
label_quantity = [Label(root, text="Quantity of Iteam:")]
entry_quantity = [Entry(root)]
for label_quantity, entry_quantity in zip(label_quantity, entry_quantity):
    label_quantity.pack()
    entry_quantity.pack()
    
label_price = [Label(root, text="Price of Iteam:")]
entry_price = [Entry(root)]
for label_price, entry_price in zip(label_price, entry_price):
    label_price.pack()
    entry_price.pack()
    
def adding2list() :
    Main_List.append(entry.get())
    Quantity_List.append(entry_quantity.get())
    Price_List.append(entry_price.get())
    update_list()
    
def update_list():
    txt_output.insert(END, Main_List[-1] + "\n")
    txt_quantity.insert(END, Quantity_List[-1] + "\n")
    txt_price.insert(END, Price_List[-1] + "\n")
    
def remove_list():
    Main_List.remove(entry.get())
    txt_output.delete("end-2l","end-1l")
    txt_quantity.delete("end-2l","end-1l")
    txt_price.delete("end-2l","end-1l")
    
    

    
adding2list = Button(root, text="Add", command=adding2list)
adding2list.pack(anchor=N)

remove_list = Button(root, text="remove", command= remove_list)
remove_list.pack(anchor=N)
    
txt_output = Text(root, height = 30, width = 50,)
txt_output.pack(pady=(0,0), padx=(0,0))
txt_output.place(x=0, y=250)

txt_quantity = Text(root, height = 30, width = 50,)
txt_quantity.pack(pady=(0,0), padx=(0,0))

txt_price = Text(root, height = 30, width = 50)
txt_price.pack(pady=(0,0), padx=(0,0))
txt_price.place(x=1500, y=250)

Main_List= ["Iteam"]
txt_output.insert(END, Main_List[0] + "\n")

Quantity_List= ["Quantity"]
txt_quantity.insert(END, Quantity_List[0] + '\n')

Price_List= ["Price"]
txt_price.insert(END, Price_List[0] + "\n")   

# f = open('item_cost.txt', 'r')

# List_of_Lines = f.readlines()

# print(List_of_Lines[0])

# for line in List_of_Lines:
#     List_of_Lines = line.split(",")
#     Main_List.append(List_of_Lines(0))
#     Price_List.append(List_of_Lines(1))
f = open('item_cost.txt', 'r')
    
list_ = open('item_cost.txt').read().split()

print(list_[0])

for line in list_:
    Main_List.append(list_[0])
    Price_List.append(list_[1])

root.mainloop()