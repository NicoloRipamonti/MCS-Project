import numpy as np
import matplotlib.pylab as plt
import math
import random
import time
from scipy.fftpack import dct

"""
dct_manual(x)
funzione che prende in input una lista di int e ritorna
un'applicazione di DCT alla stessa
"""
def dct_manual(x):
    N = len(x)

    print(type(x[0]))
    c = []
    
    for k in range(0, N):
        somma = 0
        for i in range(0, N):
            somma = somma + (x[i] * math.cos(math.pi * k * (2 * i + 1) / (2 * N)))
    
        if k == 0:
            alpha = math.sqrt(1 / N)
        else:
            alpha = math.sqrt(2 / N)
            
        c.append(somma * alpha)
            
    return c



"""
dct_manual_2d(x)
funzione che prende in input una matrice 2D
e applica per righe e per colonne la DCT (DCT2)
"""
def dct_manual_2d(x):
    return dct_manual(np.transpose(dct_manual(np.transpose(x))))



"""
dct_fftpack_2d(x)
funzione che lancia la DCT implementata in scipy.fftpack
su matrici 2D
"""
def dct_fftpack_2d(x):
    return dct(np.transpose(dct(np.transpose(x), type = 2, norm = 'ortho')), \
               type = 2, norm='ortho')


"""
test1d()
metodo che effettua dei test sulla funzione implementata in dct_manual(x),
in particolare controlla che l'output su un vettore di prova sia 
uguale a quello ritornato dalla funzione dct(x) di scipy.fftpack
"""
def test1d():
    test = [231, 32, 233, 161, 24, 71, 140, 245]
     
    test_dct = dct(test, type = 2, norm='ortho')
    
    print("1D - Libreria: ")
    print(test_dct[0], test_dct[1])
    
    test_dct = dct_manual(test)
    
    print("1D - Implementazione: ")
    print(test_dct[0], test_dct[1])
    
    
    
"""
test2d()
metodo che effettua dei test sulla funzione implementata in dct_manual_2d(x),
in particolare controlla che l'output su un vettore di prova sia 
uguale a quello ritornato dalla funzione dct_fftpack_2d(x)
"""
def test2d():
    test = [[231, 32, 233, 161, 24, 71, 140, 245], 
            [247, 40, 248, 245, 124, 204, 36, 107],
            [234, 202, 245, 167, 9, 217, 239, 173],
            [193, 190, 100, 167, 43, 180, 8, 70],
            [11, 24, 210, 177, 81, 243, 8, 112],
            [97, 195, 203, 47, 125, 114, 165, 181],
            [193, 70, 174, 167, 41, 30, 127, 245],
            [87, 149, 57, 192, 65, 129, 178, 228]]
    
    test_dct = dct_fftpack_2d(test)
    
    print("2D - Libreria: ")
    print(test_dct[0][0], test_dct[0][1])
    
    test_dct = dct_manual_2d(test)
    
    print("2D - Implementazione: ")
    print(test_dct[0][0], test_dct[0][1])
    
    

"""
matrice_random(dim)
funzione che ritorna una matrice composta da numeri casuali di dimensione dim
"""
def matrice_random(dim):
    img = np.arange(dim * dim).reshape(int(dim), int(dim))
    
    m = img.shape[0]
    
    for i in range(0, m):
        for j in range(0, m):
            img[i][j] = random.randrange(256)
            
    img[0][0] = random.randrange(256)
            
    return img


"""
plot(dimensioni, tempi_manual, tempi_scipy)
metodo che crea un plot confrontando i tempi di esecuzione delle due funzioni
"""
def plot(dimensioni, tempi_manual, tempi_scipy):
    plt.plot(dimensioni, tempi_manual, label = 'Tempi manual')
    plt.plot(dimensioni, tempi_scipy, label = 'Tempi Scipy')
    plt.legend()
    plt.xlabel("Dimensione matrici")
    plt.ylabel("Tempo esecuzione")
    plt.xlim(dimensioni[0], dimensioni[len(dimensioni) - 1] + 10)
    plt.ylim(0, tempi_manual[len(tempi_manual) - 1] + 0.4)

    from matplotlib import pyplot
    
    pyplot.savefig('confronto_implementazioni.png', bbox_inches='tight',  dpi=200)


############################### main() ####################################
    
def main():
    test1d()
    test2d()
    
    tempi_scipy = []
    tempi_manual = []
    dimensioni = []
    
    dim = 100
    while (dim <= 1000):
        img = matrice_random(dim)
        
        time1 = time.time()
        dct_fftpack_2d(img)
        time2 = time.time()
        
        tempi_scipy.append(time2 - time1)
        
        time1 = time.time()
        dct_manual_2d(img)
        time2 = time.time()
        
        tempi_manual.append(time2 - time1)
        
        dimensioni.append(dim)
        
        dim += 100
        
    plot(dimensioni, tempi_manual, tempi_scipy)
    print('Tempi Scipy: ')
    print(tempi_scipy)
    print('Tempi manual: ')
    print(tempi_manual)
    
############################################################################


if __name__ == "__main__":
    main()