from tkinter import *
import tkinter as tk
#import my local module
import File_Transfer_App_GUI


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define max and min size of frame
        self.master = master
        self.master.minsize(1000, 300)
        self.master.maxsize(1000, 300)
        # give the master frame a name
        self.master.title("Daily File Transfer")
        # give it a background color
        self.master.configure(bg="#69B0B0")

        File_Transfer_App_GUI.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
