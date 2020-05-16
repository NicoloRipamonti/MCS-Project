from tkinter import *
from tkinter import ttk 
from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
from tkinter.messagebox import showerror
from PIL import Image
import numpy as np
import os
import cv2

file_path = ""
img = []

def main_function(f, d) :
    if d < 0 or d > 2 * f - 2:
        showerror("Errore", "d dev'essere compresa fra 0 e 2F-2")
        
    global img
    img = cv2.imread(os.path.basename(file_path), 0)

    print(img)

    
######## open file ##########

def open_file(root, btn2): 
    file = askopenfile(mode ='r', filetypes =[('Immagine bmp - toni di grigio', '*.bmp')])
    w = Label(root, text="File caricato: " + os.path.basename(file.name), justify=CENTER)
    w.pack()
    global file_path
    file_path = file.name
    btn2.configure(state=NORMAL)

######## main funct #########

def main():
    root = Tk(className='Scegli file') 
    root.geometry('350x250') 
    
    w = Label(root, text="\nBenvento nel programma di Lorenzo e Nicolò!\nQua avverranno le magie...", justify=CENTER)
    w.pack()
    
    btn = Button(root, text = 'Apri file', command = lambda:open_file(root, btn2)) 
    
    info = Label(root, text="", justify=CENTER)
    info.pack()
    
    btn.pack(side = TOP, pady = 10) 
    
    var_F = StringVar(root)
    var_F.set("1")
    spin_F = Spinbox(root, from_=0, to=100, width=5,textvariable = var_F)
    
    spin_F.pack()
    
    var_d = StringVar(root)
    var_d.set("0")
    spin_d = Spinbox(root, from_=0, to=100, width=5, textvariable = var_d)
    
    spin_d.pack()
    
    btn2 = Button(root, text ='Avvia', state=DISABLED, command = lambda:main_function(int(spin_F.get()), int(spin_d.get()), ))
    
    btn2.pack(side = TOP, pady = 10)
    
    
    
    mainloop() 
    
###############################################################################

if __name__ == "__main__":
    main()





