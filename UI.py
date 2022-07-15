import tkinter
from tkinter import *
from tkinter import messagebox
# import data_training
import data_collection
#from playsound import playsound
import os
#import  audioplayer
global NOTIFY
global EVENT_OBJ
from pygame import mixer


class MyDialog:
    obj_flag = False
    def __init__(self, parent):
        if not MyDialog.obj_flag:
            MyDialog.obj_flag = True
            top = self.top = Toplevel(parent)

            Label(top, text="Value").pack()
            self.name = None
            self.e = Entry(top)
            self.e.pack(padx=5)

            b = Button(top, text="OK", command=self.ok)
            b.pack(pady=5)
            MyDialog.obj_flag=False

    def ok(self):
        print("value is", self.e.get())
        self.name = self.e.get()
        self.top.destroy()

    def get_name(self):
        return self.name


def close_button_callback():
    mainwindow.destroy()
    # playsound(os.path.join(os.getcwd(),'kgf.mp3'))

def collection_callback():
    button_off()
    toplevel_window = MyDialog(mainwindow)

    mainwindow.wait_window(toplevel_window.top)
    name = toplevel_window.get_name()
    if not name:
        messagebox.showerror("INPUT ERROR","Please ernrt a n=valid name")
    else:
        print(name)
        data_collection.data_collection(name=name)
    # exec(open("data_collection.py").read())
    button_on()
    return
def training_callback():
    button_off()
    exec(open("data_training.py").read())
    button_on()

def inference_callback():
    while True:
        msg = "Do you want to check agian"
        if messagebox.askyesno(message=msg):
            button_off()
            exec(open("inference.py").read())
            button_on()
        else:
            break

    #def call_infernce():
    ## createinfin new window
        

def modify_output_text(perd):
     output_text.set(perd)
     if pe == 'dkjfgh':
         output_label.config(fg='green')





def button_off():
    collections_button.config(state=DISABLED)
    #close_button.config(state=DISABLED)
    training_button.config(state=DISABLED)
    inference_button.config(state=DISABLED)

def button_on():
    close_button.config(state=NORMAL)
    collections_button.config(state=NORMAL)
    training_button.config(state=NORMAL)
    inference_button.config(state=NORMAL)





mainwindow = tkinter.Tk()
mainwindow.title('Emotion Detection Music')
mainwindow_height = '1280'
mainwindow_width = '720'
MAINFRAME = Frame(mainwindow, bg='white', width=mainwindow_height, height=mainwindow_width)
MAINFRAME.pack()
mainwindow.geometry(f'{mainwindow_height}x{mainwindow_width}')



# #Background image
bg=PhotoImage(file="Screenshot (258).png",)
bg_label=Label(master=MAINFRAME, image=bg)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)


# BUtton creation
button_frame = Frame(master=MAINFRAME, bg='white', width=60, height=60)

collections_button = Button(master=button_frame, text="Data Collection",command=collection_callback,bg= "CYAN")
training_button = Button(master=button_frame, text="Train the Data",command=training_callback,bg= "CYAN")
inference_button = Button(master=button_frame, text="Run", command=inference_callback,bg= "green")
close_button = Button(master=button_frame, text="Close", bg='red', command=close_button_callback)

ipax=20
ipay=20
pax=2
pay=5


collections_button.pack(in_=button_frame, side="left", ipadx=ipax, ipady=ipay, padx=pax, pady=pay)
training_button.pack(in_=button_frame, side="left", ipadx=ipax, ipady=ipay, padx=pax, pady=pay)
inference_button.pack(in_=button_frame, side="left", ipadx=ipax, ipady=ipay, padx=pax, pady=pay)
close_button.pack(in_=button_frame, side="bottom", ipadx=ipax, ipady=ipay, padx=pax, pady=pay)

button_frame.place(x=425, y=400, in_=MAINFRAME)


mainwindow.mainloop()





