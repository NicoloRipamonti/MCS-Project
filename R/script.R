library(Matrix)
library(e1071)
library(bigmemory)

A = readMM('../Matrici/ex15.mtx')

start_time <- Sys.time()
C = Cholesky(A)
print(Sys.time() - start_time)
