#include <iostream>
#include <Eigen/Dense>
#include <unsupported/Eigen/SparseExtra>
#include <Eigen/SparseCholesky>
#include <chrono>

using namespace std;
using namespace Eigen;
using namespace chrono;

int main(int argc, char** argv)
{	
    cout << endl;

    for (int i = 1; i < argc; ++i) {
		
        cout << "Cholesky con " << argv[i] << endl;		
		//Salvo il tempo corrente
        steady_clock::time_point begin = steady_clock::now();

		//Dichiaro una matrice sparsa di double chiamata A
        SparseMatrix<double> A;
		
		//Carico su A la matrice *it corrente data dall'iteratore
        loadMarket(A, argv[i]);
		
		//Creo vettore riga lungo righe di A composto da soli uno
        VectorXd xe = VectorXd::Constant(A.rows(), 1);

		//Calcolo b come prodotto fra A e xe (selfadjointView<Lower> specifica che la matrice A è
		//definita solo inferiormente (essendo simmetrica))
        VectorXd b = A.selfadjointView<Lower>() * xe;
		
		steady_clock::time_point end = steady_clock::now();
		
		//Stampo il tempo trascorso
        cout << "Time Setup = " << duration_cast<nanoseconds>(end - begin).count() << "ns" << endl;
		begin = steady_clock::now();


		//Calcolo la Cholesky con la funzione SimplicialLDLT
        SimplicialLDLT<SparseMatrix<double>> chol(A);
		
		end = steady_clock::now();
		
		//Stampo il tempo trascorso
        cout << "Time Cholesky = " << duration_cast<nanoseconds>(end - begin).count() << "ns" << endl;
		begin = steady_clock::now();
		//Trovo la soluzione x con la funzione solve
        VectorXd x = chol.solve(b);
		end = steady_clock::now();
		
		//Stampo il tempo trascorso
        cout << "Time Resolve = " << duration_cast<nanoseconds>(end - begin).count() << "ns" << endl;

	
		//Calcolo errore relativo
        double relative_error = (x - xe).norm() / (xe).norm();
        
        cout << "Relative error = " << relative_error << endl;

        cout << endl << "****" << endl << endl;
    }
}