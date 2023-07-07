from tkinter import *


class Begueradj(Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.main_queue = ["read", "clean dishes", "wash car"]
        self.r = 0
        self.initialize_user_interface()


    def initialize_user_interface(self):
        self.parent.title("Update GUI")
        self.parent.grid_rowconfigure(0, weight = 1)
        self.parent.grid_columnconfigure(0, weight = 1)

        for e in self.main_queue:
            tkinter.Label(self.parent, anchor = tkinter.W, text = e).grid(row = self.r, sticky = tkinter.W)
            self.r+=1
        self.entry_text = tkinter.Entry(self.parent)
        self.entry_text.grid(row = 0, column = 1)
        self.button_update = tkinter.Button(self.parent, text = "Update", command = self.update_gui).grid(row = 1, column = 1, sticky = tkinter.E)

    def update_gui(self):
        self.r+=1
        self.main_queue.append(self.entry_text.get())
        tkinter.Label(self.parent, anchor = tkinter.W, text = self.entry_text.get()).grid(row = self.r, sticky = tkinter.W)

tkinter = Tk()

def main():
    root = tkinter.Tk()
    b = Begueradj(root)
    root.mainloop()

if __name__ == "__main__":
    main()