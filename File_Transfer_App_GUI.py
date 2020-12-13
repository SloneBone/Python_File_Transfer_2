from tkinter import *
import tkinter as tk

#importing my local module
import File_Transfer_App_Fx


def load_gui(self):
      
    # create an entry text box for source button
    self.custom_source = StringVar()
    # set text box to a default string
    self.custom_source.set('Select a Source Directory')
    # set the width to 60 characters
    self.text_source = tk.Entry(self.master, width=60, textvariable=self.custom_source)
    self.text_source.grid(row=0, column=0, rowspan=1, columnspan=2, padx=(5, 0), pady=(10, 20))

    # create an entry text box for destination button
    self.custom_dest = StringVar()
    # set text box to a default string
    self.custom_dest.set('Select a Destination Directory')
    # set the width to 60 characters
    self.text_dest = tk.Entry(self.master, width=60, textvariable=self.custom_dest)
    self.text_dest.grid(row=0, column=3, rowspan=1, columnspan=2, padx=(5, 0), pady=(10, 20))

    # create and place a source button
    self.button_source = tk.Button(self.master, bg= "yellow", width=12, height=1, text="Source", command=lambda: File_Transfer_App_Fx.get_source(self))
    self.button_source.grid(row=0, column=2, padx=(10, 0), pady=(10, 20))

    # create and place a destination button
    self.button_dest = tk.Button(self.master, bg= "yellow", width=12, height=1, text="Destination", command=lambda: File_Transfer_App_Fx.get_dest(self))
    self.button_dest.grid(row=0, column=5, padx=(10, 0), pady=(10, 20))

    
    # Create Transfer File button
    self.button_transfer = tk.Button(self.master, bg="green", fg="white", width=16, height=2, text="Transfer Files", command=lambda: File_Transfer_App_Fx.Copy_Files(self, self.custom_source, self.custom_dest))
    self.button_transfer.grid(row=8, column=2, padx=(0, 0), pady=(10, 10))

    # Creating 'Close Program' Button
    self.button_done = tk.Button(self.master, bg="red", fg="white", width=16, height=2, text="Close Program",command=lambda: File_Transfer_App_Fx.close(self))
    self.button_done.grid(row=10, column=2, padx=(0, 0), pady=(10, 10))

  
if __name__ == "__main__":
    pass
