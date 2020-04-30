from scipy.io import mmread
from scipy import linalg
from scipy.sparse import linalg as sparselinalg
import numpy as np
import time

start = time.time()

A = mmread('../Matrici/ex15.mtx')

xe = np.ones(np.size(A,0))

b = A.dot(xe)

R = linalg.cholesky(A.toarray(), lower=False)

y = sparselinalg.spsolve(R.transpose(), b)

y = np.linalg.solve(R.transpose(), b)

x = np.linalg.solve(R, y)

errore = np.linalg.norm(x - xe) / np.linalg.norm(xe)

t = time.time() - start

print(str(t) + ' seconds')

print('errore: ' + str(errore))