#include <iostream>
#include <Eigen/Dense>
#include <unsupported/Eigen/SparseExtra>
#include <Eigen/SparseCholesky>
#include <chrono>

using namespace std;
using namespace Eigen;

int main()
{

    list<string> listOfMatrixes = {"../Matrici/ex15.mtx",
                                   "../Matrici/shallow_water1.mtx"};

    //Create an iterator of std::list
    std::list<string>::iterator it;
    cout << endl;

    for (it = listOfMatrixes.begin(); it != listOfMatrixes.end(); it++) {
		
        chrono::steady_clock::time_point begin = chrono::steady_clock::now();

        SparseMatrix<double> A;
		
        loadMarket(A, *it);

        cout << "Cholesky con " << *it << endl;

        VectorXd xe = VectorXd::Constant(A.rows(), 1);

        VectorXd b = A.selfadjointView<Lower>() * xe;

        LDLT<SparseMatrix<double>> chol(A);

        VectorXd x = chol.solve(b);

        chrono::steady_clock::time_point end = chrono::steady_clock::now();
		
        cout << "Time difference = " << chrono::duration_cast<chrono::seconds>(end - begin).count() << "s" << endl;

        double relative_error = (x - xe).norm() / (xe).norm();
        
        cout << "Relative error = " << relative_error << endl;

        cout << endl << "****" << endl << endl;
    }
}