from tkinter import *
from tkinter import ttk 
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
from tkinter.messagebox import showerror
from PIL import Image
import numpy as np

file = ""

def main_function() :
    f = int(spin_F.get())
    d = int(spin_d.get())

    if d < 0 or d > 2 * f - 2:
        showerror("Errore", "d dev'essere compresa fra 0 e 2F-2")

    im = Image.open(file.name)
    p = np.array(im)

    

def open_file(): 
    file = askopenfile(mode ='r', filetypes =[('Immagine bmp - toni di grigio', '*.bmp')]) 


root = Tk(className='Scegli file') 
root.geometry('550x250') 

w = Label(root, text="\nBenvento nel programma di Lorenzo e Nicolò!\nQua avverranno le magie...", justify=CENTER)
w.pack()

btn = Button(root, text = 'Open', command = lambda:open_file()) 

btn.pack(side = TOP, pady = 10) 

spin_F = Spinbox(root, from_=0, to=100, width=5)

spin_F.pack()

spin_d = Spinbox(root, from_=0, to=100, width=5)

spin_d.pack()

btn = Button(root, text ='Avvia', command = lambda:main_function())

btn.pack(side = TOP, pady = 10) 

mainloop() 




