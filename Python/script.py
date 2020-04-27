from scipy.io import mmread
from scipy import linalg
import time

ex15 = mmread('../Matrici/ex15.mtx')

ex15_array = ex15.toarray()

start = time.time()
L = linalg.cholesky(ex15_array, lower=True)
t = time.time() - start

print(str(t) + ' seconds')