#include <iostream>
#include <Eigen/Dense>
#include <unsupported/Eigen/SparseExtra>
#include <Eigen/SparseCholesky>
#include <chrono>

using namespace std;
using namespace Eigen;

int main()
{

	//Creo lista di path di matrici su cui lanciare lo script
    list<string> listOfMatrixes = {"../Matrici/ex15.mtx",
                                   "../Matrici/shallow_water1.mtx"};

    //Creo iteratore che cicla sulla lista
    std::list<string>::iterator it;
	
    cout << endl;

    for (it = listOfMatrixes.begin(); it != listOfMatrixes.end(); it++) {
		//Salvo il tempo corrente
        chrono::steady_clock::time_point begin = chrono::steady_clock::now();

		//Dichiaro una matrice sparsa di double chiamata A
        SparseMatrix<double> A;
		
		//Carico su A la matrice *it corrente data dall'iteratore
        loadMarket(A, *it);

		
        cout << "Cholesky con " << *it << endl;

		//Creo vettore riga lungo righe di A composto da soli uno
        VectorXd xe = VectorXd::Constant(A.rows(), 1);

		//Calcolo b come prodotto fra A e xe (selfadjointView<Lower> specifica che la matrice A è
		//definita solo inferiormente (essendo simmetrica))
        VectorXd b = A.selfadjointView<Lower>() * xe;

		//Calcolo la Cholesky con la funzione SimplicialLDLT
        SimplicialLDLT<SparseMatrix<double>> chol(A);

		//Trovo la soluzione x con la funzione solve
        VectorXd x = chol.solve(b);

		//Salvo il tempo corrente (per calcolare la differenza con quello iniziale)
        chrono::steady_clock::time_point end = chrono::steady_clock::now();
		
		//Stampo il tempo trascorso
        cout << "Time difference = " << chrono::duration_cast<chrono::seconds>(end - begin).count() << "s" << endl;

		//Calcolo errore relativo
        double relative_error = (x - xe).norm() / (xe).norm();
        
        cout << "Relative error = " << relative_error << endl;

        cout << endl << "****" << endl << endl;
    }
}