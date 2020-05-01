# Metodi del Calcolo Scientifico

Relazioni e implementazioni Progetto 1 e Progetto ? 

## Progetto 1 - Cholesky

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

| Errore             | Matlab       | C++ (Win bash) | C++ (Ubuntu bash) |      R     |
| -------------      |:------------:|:--------------:|:-----------------:|:----------:|
| ex15.mtx           |  8.5736e-07  |   6.6293-07    |    7.2664e-07     | 5.1994e-07 |
| shallow_water1.mtx |  3.1985e-16  |   2.4323-16    |    2.4293e-16     | 2.5329e-16 |
| cfd1.mtx           |  2.7864e-13  |   2.5442-12    |    2.5044e-12     | 3.9818e-11 |
| cfd2.mtx           |  6.8098e-13  |   5.3424-13    |    5.5531e-12     | 1.7934e-11 |
| parabolic_fem.mtx  | `out of mem` |   2.9088-12    |    2.4557e-12     |`out of mem`|
| apache2.mtx        | `out of mem` | `std::badalloc`|    9.8846e-11     |`out of mem`|  

| Memoria            | R            | C++ Win         | C++ Lin | Matlab       |
|--------------------|--------------|-----------------|---------|--------------|
| cfd1.mtx           | 953MB        | 461MB           | 450MB   | 1206MB       |
| cfd2.mtx           | 1874MB       | 895MB           | 887.6MB | 2409MB       |
| shallow_water1.mtx | 276MB        | 36MB            | 35.8MB  | 351MB        |
| ex15.mtx           | 3.1MB        | 3MB             | 4.1MB   | 27MB         |
| parabolic_fem.mtx  | `out of mem` | 485MB           | 502MB   | `out of mem` |
| apache2.mtx        | `out of mem` | `std::badalloc` | 2619MB  | `out of mem` |

---

| Tempo totale       | R           | C++ Win        | C++ Lin     | Matlab      |
|--------------------|-------------|----------------|-------------|-------------|
| cfd1.mtx           | 82.6357 s   | 202.4469 s     | 218.9470 s  | 7.6486 s    |
| cfd2.mtx           | 231.3900 s  | 974.5525 s     | 1064.9390 s | 34.4108s    |
| shallow_water1.mtx | 21.5715 s   | 5.4666 s       | 9.5677 s    | 5.2170 s    |
| ex15.mtx           | 0.2315 s    | 0.5718 s       | 0.6481 s    | 0.1943 s    |
| parabolic_fem.mtx  | out of mem' | 85.8982 s      | 75.7502 s   | out of mem' |
| apache2.mtx        | out of mem' | std::badalloc' | 1611.8161 s | out of mem' |

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

$-b \pm \sqrt{b^2 - 4ac} \over 2a$

## License
[MIT](https://choosealicense.com/licenses/mit/)
