# -*- coding: utf-8 -*-
"""
Created on Wed May 20 13:52:33 2020

@author: loren
"""
import numpy as np
import matplotlib.pylab as plt
import math
import random

img = []
img_compressa_slow = []
img_compressa_fast = []

def dct_manual(img):
    m = img.shape[0]
    n = img.shape[1]
    dct = np.zeros((m, n))
    
    for i in range(0, m):
        for j in range(0, n):
            if i == 0:
                ci = 1 / math.sqrt(m)
            else:
                ci = math.sqrt(2) / math.sqrt(m)
                
            if j == 0:
                cj = 1 / math.sqrt(n)
            else:
                cj = math.sqrt(2) / math.sqrt(n)
                
            somma = 0
            
            for k in range(0, m):
                for l in range(0, n):
                    dct1 = img[k][l] * \
                    math.cos((2 * k + 1) * i * math.pi / (2 * m)) * \
                    math.cos((2 * l + 1) * j * math.pi / (2 * n))
                    
                    somma += dct1
            
            dct[i][j] = ci * cj * somma;
            
    return dct

def matrice_random(dim):
    img = np.arange(dim * dim).reshape(int(dim), int(dim))
    
    m = img.shape[0]
    
    for i in range(0, m):
        for j in range(0, m):
            img[i][j] = random.randrange(256)
            
    img[0][0] = random.randrange(256)
            
    return img


def main():
    global img, img_compressa_slow, img_compressa_fast
    
    for i in range(1, 2):
        dim = i * 10
        img = matrice_random(dim)
        
        img_compressa_slow = dct_manual(np.transpose(dct_manual(np.transpose(img))))
        
        from scipy.fftpack import dct
        
        img_compressa_fast = dct(np.transpose(dct(np.transpose(img), norm='ortho')), norm='ortho')
    
    
























if __name__ == "__main__":
    main()