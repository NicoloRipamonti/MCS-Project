# Metodi del Calcolo Scientifico

Relazioni e implementazioni Progetto 1 e Progetto ? 

## Progetto 1 - Cholesky

L'obiettivo del primo progetto è quello di implementare algoritmi per la risoluzione di matrici sparse simmetriche e definite positive di grandi dimensioni, per farlo abbiamo utilizzato quattro ambienti:

* Matlab
* C++
* C++ (su Ubuntu 20.04 LTS installato tramite WSL)
* R

Come leggere i risulati?

* Time setup  
Tempo trascorso per leggere la matrice, creare la matrice _xe_ e la _B_.
* Time Cholesky  
Tempo trascorso per calcolare la matrice di Cholesky (triangolare inferiore) _R_.
* Time resolve  
Tempo trascorso per calcolare la soluzione _x_

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

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
