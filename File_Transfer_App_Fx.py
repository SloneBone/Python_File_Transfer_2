import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import datetime
import shutil
import time
import os

#Creating a function to get Source folder from user using askdirectory
#and input it in corresponding text box
def get_source(self):
    self.text_source.delete(0, 60)
    self.custom_source = filedialog.askdirectory()
    self.text_source.insert(0, self.custom_source)

#Creating a function to get Destination folder from user
#and input it in correspondin text box
def get_dest(self):
    self.text_dest.delete(0, 60)
    self.custom_dest = filedialog.askdirectory()
    self.text_dest.insert(0, self.custom_dest)


def Copy_Files(self, source, destination):
    # declare variables for current run time and 24 hours ago
    now = datetime.datetime.now()
    ago = now - datetime.timedelta(hours=24)
    print('The following .txt files were modified in the last 24 hours: \n')

    # loop through files in the source parameter
    for files in os.listdir(source):
        # if the files end with '.txt', create variables with a path and stats
        if files.endswith('.txt'):
            path = os.path.join(source, files)
            st = os.stat(path)
            # create a variable with the file's timestamp from its stats
            mtime = datetime.datetime.fromtimestamp(st.st_mtime)
            # compare the file's modified time with 24 hours ago
            if mtime > ago:
                # print the file and when it was last modified
                print('{} ~ last modified {}'.format(path, mtime))
                # use os.path.join to create an absolute path
                file_source = os.path.join(source, files)
                file_destination = os.path.join(destination, files)
                # move the files using the absolute path
                shutil.copy(file_source, file_destination)
                # print what was moved successfully and to where
                print("\tMoved {} to {}.\n".format(files, destination))
                # Adding a Pop up message to show succesful transfer
                # Note: this msg happens on every succesful file transfer
                # On lager scale I would probalby just move it ouside of loop
                messagebox.showinfo("File Transfer", "File(s) copied successfully!")


    

#creating a function to close program
def close(self):
    if messagebox.askokcancel("Exit Program", "Are you sure you want to close the application?"):
        self.master.destroy()
        os._exit(0)



if __name__ == "__main__":
    pass
