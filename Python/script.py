from scipy.io import mmread
from scipy import linalg
import time

ex15 = mmread('../Matrici/ex15.mtx')

A = ex15.toarray()

start = time.time()

R = linalg.cholesky(A, lower=True)

t = time.time() - start

print(str(t) + ' seconds')