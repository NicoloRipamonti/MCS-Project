from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showerror
from PIL import Image, ImageTk
import numpy as np
import os
import cv2
from scipy.fftpack import dct, idct

import matplotlib.pylab as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


file_path = ""
img = []

lista_blocchi = []
lista_blocchi_inversa = []
img_compressa = []
colonne = []

def suddividi(img, f):
    global lista_blocchi

    i = 0
    j = 0
    
    while (i + f < img.shape[0]):
        while(j + f < img.shape[1]):
            blocco = img[i:i+f,j:j+f]
            lista_blocchi.append(blocco)
            j = j + f
        i = i + f
        j = 0

    return img

def applica_dct(img, d, f_dim):
    global lista_blocchi_inversa
    global img_compressa
    
    lista_blocchi_inversa = []
    
    for f in lista_blocchi:
        c = dct(np.transpose(dct(np.transpose(f), norm='ortho')), norm='ortho')
    
        for k in range(0, c.shape[0]):
            for l in range(0, c.shape[1]):
                if k + l >= d:
                    c[k, l] = 0
                    
        ff = idct(np.transpose(idct(np.transpose(c), norm='ortho')), norm='ortho')

        for i in range(0, ff.shape[0]):
            for j in range(0, ff.shape[1]):
                ff[i,j] = int(ff[i,j])

                if ff[i, j] < 0:
                    ff[i,j] = 0
                elif ff[i,j] > 255:
                    ff[i,j] = 255

        lista_blocchi_inversa.append(ff)
        
    
    i = 0
    j = 0
    index = 1
    
    col = lista_blocchi_inversa[0]

    global colonne
    colonne = []
    
    while (i + f_dim< img.shape[0]):
        while(j + f_dim < img.shape[1]):
            j = j + f_dim
            if j + f_dim < img.shape[1]:
                col = np.hstack((col, lista_blocchi_inversa[index]))
                index = index + 1

        i = i + f_dim
        j = 0
        colonne.append(col)
        if index < len(lista_blocchi_inversa):
            col = lista_blocchi_inversa[index]
        index = index + 1

    img_compressa = colonne[0]

    for i in range(1, len(colonne)):
        img_compressa = np.vstack((img_compressa, colonne[i]))
        
    img_compressa = img_compressa.astype(np.uint8)
    cv2.imwrite('montagna_gay.jpg', img_compressa)
    
    
    #f.savefig("bmp_vs_jpg.pdf", bbox_inches='tight')
    
    root = Tk()
    root.wm_title("Embedding in Tk")
    
    fig = Figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    fig.add_subplot(121).imshow(img)
    fig.add_subplot(122).imshow(img_compressa)
    
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    
    
    def on_key_press(event):
        print("you pressed {}".format(event.key))
        key_press_handler(event, canvas, toolbar)
    
    
    canvas.mpl_connect("key_press_event", on_key_press)
    
    button = Button(master=root, text="Quit", command=root.quit)
    
    # Packing order is important. Widgets are processed sequentially and if there
    # is no space left, because the window is too small, they are not displayed.
    # The canvas is rather flexible in its size, so we pack it last which makes
    # sure the UI controls are displayed as long as possible.
    button.pack(side=BOTTOM)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    
    mainloop()
    
    
def main_function(f, d) :
    if d < 0 or d > 2 * f - 2:
        showerror("Errore", "d dev'essere compresa fra 0 e 2F-2")

    global img
    img = cv2.imread(os.path.basename("montagna.bmp"), 0)

    img_suddivisa = suddividi(img, f)

    applica_dct(img_suddivisa, d, f)



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
    var_F.set("4")
    spin_F = Spinbox(root, from_=0, to=100, width=5,textvariable = var_F)

    spin_F.pack()

    var_d = StringVar(root)
    var_d.set("3")
    spin_d = Spinbox(root, from_=0, to=100, width=5, textvariable = var_d)

    spin_d.pack()

    #state=DISABLED
    btn2 = Button(root, text ='Avvia', command = lambda:main_function(int(spin_F.get()), int(spin_d.get()), ))

    btn2.pack(side = TOP, pady = 10)



    mainloop()

###############################################################################

if __name__ == "__main__":
    main()
