# Metodi del Calcolo Scientifico

Relazioni e implementazioni Progetto 1 e Progetto ? 

## Progetto 1 - Cholesky

L'obiettivo del primo progetto è quello di implementare algoritmi per la risoluzione di matrici sparse simmetriche e definite positive di grandi dimensioni, per farlo abbiamo utilizzato quattro ambienti:

* Matlab
* C++
* C++ (su Ubuntu 20.04 LTS installato tramite WSL)
* R

### Matlab

Per eseguire lo script su Matlab, caricare nel workspace la matrice da trattare con:

```bash
load('cfd2.mat')
```
Successivamente lanciare lo script.

### C++ 

Per eseguire lo script su C++, compilarlo attraverso

```bash
g++ -I eigen-eigen-323c052e1731 script.cpp -o script
```

e lanciarlo passando come argomento la matrice da trattare, ad esempio:

```bash
./script "..Matrici/cfd2.mtx"
```


## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
