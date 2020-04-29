#include <iostream>
#include <Eigen/Dense>
#include <unsupported/Eigen/SparseExtra>
#include <Eigen/SparseCholesky>
#include <chrono>

using namespace std;
using namespace Eigen;

int main()
{
    chrono::steady_clock::time_point begin = chrono::steady_clock::now();

    SparseMatrix<double> A;
    loadMarket(A, "../Matrici/apache2.mtx");
	
	cout << "Operazioni con apache2.mtx" << endl;

    VectorXd xe = VectorXd::Constant(A.rows(), 1);

    VectorXd b = A.selfadjointView<Lower>() * xe;

    SimplicialLDLT<SparseMatrix<double>> chol(A);

    VectorXd x = chol.solve(b);

    chrono::steady_clock::time_point end = chrono::steady_clock::now();
    cout << "Time difference = " << chrono::duration_cast<chrono::milliseconds>(end - begin).count() << "ms" << endl;

    double relative_error = (x - xe).norm() / (xe).norm();

    cout << "Relative error = " << relative_error << endl;

    //errore = norm(x - xe) / norm(xe)
}