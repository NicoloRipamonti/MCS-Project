# Metodi del Calcolo Scientifico

Relazioni e implementazioni Progetto 1 e Progetto 2

## Progetto 1 - Implementazione metodo di Cholesky

L'obiettivo del primo progetto è quello di implementare algoritmi per la risoluzione di matrici sparse simmetriche e definite positive di grandi dimensioni, per farlo abbiamo utilizzato quattro ambienti:

* Matlab
* C++
* C++ (su Ubuntu 20.04 LTS installato tramite WSL)
* R

Come leggere i risulati?

* **Time setup**  
Tempo trascorso per leggere la matrice, creare la matrice _xe_ e la _B_.
* **Time Cholesky**   
Tempo trascorso per calcolare la matrice di Cholesky (triangolare inferiore) _R_.
* **Time resolve**  
Tempo trascorso per calcolare la soluzione _x_
* **Errore**  
L' errore relativo tra la soluzione calcolata _x_ e la soluzione esatta _xe_

### Matlab

Per eseguire lo script su Matlab, caricare nel workspace la matrice da trattare con:

```bash
load('cfd2.mat')
```
Successivamente lanciare lo script.

Su console verranno stampati i risultati come segue:

```bash
>> script
Time setup:
Elapsed time is 0.001899 seconds.
Time Cholesky:
Elapsed time is 0.187418 seconds.
Time resolve:
Elapsed time is 0.005750 seconds.
Errore: 
8.5736e-07
```

### C++ 

Per eseguire lo script su C++, compilarlo attraverso

```bash
g++ -I eigen-eigen-323c052e1731 script.cpp -o script
```

e lanciarlo passando come argomento la matrice da trattare, ad esempio:

```bash
./script "..Matrici/cfd2.mtx"
```

i risulati verranno visualizzati quando il processo è terminato, un esempio è il seguente: 

```bash
Cholesky con ../Matrici/ex15.mtx
Time Setup = 0.32702s
Time Cholesky = 0.172623s
Time Resolve = 0.0133566s
Relative error = 6.62936e-07
```

### R

Per eseguire lo script su R, aprire lo script e sostituire alla linea 5 del codice il nome della matrice da trattare, ad es:

```bash
A = readMM("../Matrici/parabolic_fem.mtx")
```

i risultati verranno stampati su console come segue:

```bash
> Errore
5.199477e-07
> Memory
3127552 bytes
> Time_Setup
Time difference of 0.08876419 secs
> Time_Chol
Time difference of 0.02691793 secs
> Time_Solving
Time difference of 0.01097298 secs
```

### Risultati

Questi sono i risultati ottenuti su Surface Book 2 (i5-7300U, 8GB RAM) lanciati in modalità energetica massime prestazioni, con il singolo programma aperto (e un task manager per controllare l'utilizzo della memoria)
| Errore             | R            | C++ Win         | C++ Lin     | Matlab       |
|--------------------|--------------|-----------------|-------------|--------------|
| cfd1.mtx           | 3.981871e-11 | 2.54423e-12     | 2.50441e-12 | 2.7864e-13   |
| cfd2.mtx           | 1.793486e-11 | 5.34245e-12     | 5.55314e-12 | 6.8098e-13   |
| shallow_water1.mtx | 2.532940e-16 | 2.43236e-16     | 2.42931e-16 | 3.1985e-16   |
| ex15.mtx           | 5.199477e-07 | 6.62936e-07     | 7.26641e-07 | 8.5736e-07   |
| parabolic_fem.mtx  | `out of mem` | 2.90885e-12     | 2.45574-e12 | `out of mem` |
| apache2.mtx        | `out of mem` | `std::badalloc` | 9.88465e-11 | `out of mem` |

---

| Memoria            | R            | C++ Win         | C++ Lin | Matlab       |
|--------------------|--------------|-----------------|---------|--------------|
| cfd1.mtx           | 953MB        | 461MB           | 450MB   | 1206MB       |
| cfd2.mtx           | 1874MB       | 895MB           | 887.6MB | 2409MB       |
| shallow_water1.mtx | 276MB        | 36MB            | 35.8MB  | 351MB        |
| ex15.mtx           | 3.1MB        | 3MB             | 4.1MB   | 27MB         |
| parabolic_fem.mtx  | `out of mem` | 485MB           | 502MB   | `out of mem` |
| apache2.mtx        | `out of mem` | `std::badalloc` | 2619MB  | `out of mem` |

---

| Tempo totale       | R            | C++ Win         | C++ Lin     | Matlab       |
|--------------------|--------------|-----------------|-------------|--------------|
| cfd1.mtx           | 82.6357 s    | 202.4469 s      | 218.9470 s  | 7.6486 s     |
| cfd2.mtx           | 231.3900 s   | 974.5525 s      | 1064.9390 s | 34.4108s     |
| shallow_water1.mtx | 21.5715 s    | 5.4666 s        | 9.5677 s    | 5.2170 s     |
| ex15.mtx           | 0.2315 s     | 0.5718 s        | 0.6481 s    | 0.1943 s     |
| parabolic_fem.mtx  | `out of mem` | 85.8982 s       | 75.7502 s   | `out of mem` |
| apache2.mtx        | `out of mem` | `std::badalloc` | 1611.8161 s | `out of mem` |


## Progetto 2 - Esperimenti su DCT

Il secondo progetto è suddiviso in due parti:

# Parte 1
L'obiettivo della prima parte è quello di confrontare l'implementazione della DCT di una libreria ad un'implementazione effettuata dal gruppo.
Come linguaggio di programmazione è stato scelto Python, la libreria in questione invece è Scipy, più precisamente si è utilizzato scipy.fftpack.dct (https://docs.scipy.org/doc/scipy/reference/generated/scipy.fftpack.dct.html

Il confronto è stato effettuato in termini di tempi su un insieme di matrici generate in modo pseudo-casuale di dimensione 100n x 100n con n che va da 1 a 10

I risultati sono stati prevedibili in quanto la libreria è risultata decisamente più veloce rispetto alla implementazione "ad-hoc".

Di seguito i risultati ottenuti su 

| Dimensione matrice  | scipy.fftpack.dct  | dct_manuale |
|---------------------|--------------------|-------------|
| 100x100             | 0.00041 s          | 0.06779s    |
| 200x200             | 0.00157 s          | 0.30789s    |
| 300x300             | 0.00217 s          | 0.75378s    |
| 400x400             | 0.00369 s          | 1.60575s    |
| 500x500             | 0.00703 s          | 2.46435s    |
| 600x600             | 0.00976 s          | 3.99684s    |
| 700x700             | 0.01821 s          | 5.74928s    |
| 800x800             | 0.01818 s          | 10.02264s   |
| 900x900             | 0.04131 s          | 13.11710s   |
| 1000x1000           | 0.03638 s          | 20.02069s   |



