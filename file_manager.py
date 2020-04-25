import os
import sys,shutil
import subprocess
from tkinter import *


root = Tk()

main = Label(root,text="File Manager")


def entry_window(rno,string):
    global e
    window=Tk()
    if(string=='open'):
        label = Label(window,text="Enter File Location")
        label.grid(row=rno,column=2)
        e = Entry(window)
        e.grid(row=rno+1,column=3)
        submit_button = Button(window,text="Submit",command = open_file)
        submit_button.grid(row=rno+2,column=3)
    if(string == 'copy'):
        global src,dest
        label = Label(window,text='Source Location')
        label.grid(row=rno+1,column=2)
        label.grid(row=3,column=2)
        src = Entry(window)
        src.grid(row=rno+2,column=2)
        label = Label(window,text='Destination Location')
        label.grid(row=rno+3,column=2)
        dest = Entry(window)
        dest.grid(row=rno+4,column=2)
        submit_button = Button(window,text="Submit",command=copy_file)
        submit_button.grid(row=rno+5,column=3)
    if(string=='verify_file'):
        label = Label(window,text="Enter File Location")
        label.grid(row=rno,column=2)
        e = Entry(window)
        e.grid(row=rno+1,column=3)
        submit_button = Button(window,text="Submit",command = check_file)
        submit_button.grid(row=rno+2,column=3)
    if(string=='verify_dir'):
        label = Label(window,text="Enter Directory Location")
        label.grid(row=rno,column=2)
        e = Entry(window)
        e.grid(row=rno+1,column=3)
        submit_button = Button(window,text="Submit",command = check_dir)
        submit_button.grid(row=rno+2,column=3)
    if(string=='list_file'):
        label = Label(window,text="Enter Directory Location")
        label.grid(row=rno,column=2)
        e = Entry(window)
        e.grid(row=rno+1,column=3)
        submit_button = Button(window,text="Submit",command = list_file)
        submit_button.grid(row=rno+2,column=3)

    if(string == 'delete_file'):
        label = Label(window,text="Enter File Location")
        label.grid(row=rno,column=2)
        e = Entry(window)
        e.grid(row=rno+1,column=3)
        submit_button = Button(window,text="Submit",command = delete_file)
        submit_button.grid(row=rno+2,column=3)
    
    if(string == 'move_file'):
        print("Chal ja bhai")
        label = Label(window,text='Source Location')
        label.grid(row=rno+1,column=2)
        label.grid(row=3,column=2)
        src = Entry(window)
        src.grid(row=rno+2,column=2)
        label = Label(window,text='Destination Location')
        label.grid(row=rno+3,column=2)
        dest = Entry(window)
        dest.grid(row=rno+4,column=2)
        print("Hy Bro")
        submit_button = Button(window,text="Submit",command=move)
        submit_button.grid(row=rno+5,column=3)

    if(string == "make_fold"):
        label = Label(window,text="Enter New Folder Location")
        label.grid(row=rno,column=2)
        e = Entry(window)
        e.grid(row=rno+1,column=3)
        submit_button = Button(window,text="Submit",command = make_fold)
        submit_button.grid(row=rno+2,column=3)

    if(string == "delete_fold"):
        label = Label(window,text="Enter Folder Location - ")
        label.grid(row=rno,column=2)
        e = Entry(window)
        e.grid(row=rno+1,column=3)
        submit_button = Button(window,text="Submit",command = delete_fold)
        submit_button.grid(row=rno+2,column=3)

    window.mainloop()


def open_file():
    global e
    file_name = e.get()
    try:
        if sys.platform == "win32":
            os.startfile(filename)
        else:
            opener ="open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, file_name])
    except:
        print("File_Not_Found")


def check_file():
    global e
    file_name = e.get()
    if os.path.isfile(file_name)==True:
        print("File Exist")
    else:
        print("This File Does Not Exist")

def check_dir():
    global e
    Dir_name = e.get()
    if os.path.isdir(Dir_name)==True:
        print("Directory Exist")
    else:
        print("This Directory Does Not Exist")

def list_file():
    global e
    Dir_name= e.get()
    try:
        print("--------------------Your Files and Directories are --------------------")
        for files in os.listdir(Dir_name):
            print(files)
        print("------------------------------------------\n\n")
    except:
        print("This Directory does not exist")

def delete_file():
    global e
    file_name = e.get()
    if os.path.isfile(file_name)==True:
        os.remove(file_name)
        print("File Deleted")
    else:
        print("File does not Exist")


def copy_file():
    global src,dest
    source = src.get()
    destination = dest.get()
    shutil.copy(source,destination)

def move():
    print("Move it move it")
    global src
    global dest
    src_file_name = src.get()
    dest_file_name = dest.get()
    shutil.move(src_file_name,dest_file_name)
    print("File Moved")
    

def make_fold():
    global e
    new_folder_name = e.get()
    os.makedirs(new_folder_name)

def delete_fold():
    global e
    folder_name = e.get()
    os.rmdir(folder_name)


open_button = Button(root,text = "Open a file",command=lambda:entry_window(1,'open'))
verify_file = Button(root,text = "Verify a file",command=lambda:entry_window(2,'verify_file'))
verify_dir = Button(root,text = "Verify a Directory",command=lambda:entry_window(3,'verify_dir'))
list_button = Button(root,text = "List all files in Directory",command=lambda : entry_window(4,'list_file'))
copy_button = Button(root,text = "Copy a File",command=lambda:entry_window(5,'copy'))
delete_button = Button(root,text = "Delete a file",command=lambda : entry_window(6,'delete_file'))
move_file  = Button(root,text="Move a file",command = lambda : entry_window(7,'move_file'))
make_folder = Button(root,text="Make a folder",command = lambda : entry_window(8,'make_fold'))
delete_folder = Button(root,text="Delete a folder", command = lambda : entry_window(8,'delete_fold'))

open_button.grid(row=1,column = 0,padx=100,pady=20,columnspan=5)
verify_file.grid(row=2,column = 0,padx=100,pady=20,columnspan=5)
verify_dir.grid(row=3,column = 0,padx=100,pady=20,columnspan=5)
list_button.grid(row=4,column = 0,padx=100,pady=20,columnspan=5)
copy_button.grid(row=5,column = 0,padx=100,pady=20,columnspan=5)
delete_button.grid(row=6,column = 0,padx=100,pady=20,columnspan=5)
move_file.grid(row=8,column = 0,padx=100,pady=20,columnspan=5)
make_folder.grid(row=9,column = 0,padx=100,pady=20,columnspan=5)
delete_folder.grid(row=10,column = 0,padx=100,pady=20,columnspan=5)


main.grid(row=0,column=0,columnspan=5)

root.mainloop()
#daishinkan/Documents/Folder