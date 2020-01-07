from tkinter import *
from tkinter.ttk import *
from tkinter import scrolledtext
import actions

#Main file - should be executed

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.master=master
        self.init_window()

    def init_window(self):
        self.master.title("Halo MCC Modloader for Steam")
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        options = Menu(menu,tearoff=False)
        options.add_command(label="Choose Directory")

        menu.add_cascade(label="Options",menu=options)

        #head menu definition


        #button definition
        quitButton = Button(self,text="Exit",command=exit)
        quitButton.place(x=0,y=0)


root = Tk()
root.geometry("400x300")

app= Window(root)

root.iconbitmap("resources/masterchief.ico")
root.mainloop()
