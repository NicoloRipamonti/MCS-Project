library(Matrix)
library(e1071)

##MATRIX EX15:


A= readMM("../Matrici/cfd1.mtx")

xe = rep(1, times = nrow(A))

b = A %*% xe

start_time <- Sys.time()
C = chol(A)
end_time <- Sys.time()

Memory = object.size(chol(A))

y = solve(t(C), b)

x = solve(C, y)

xe = as.matrix(xe)

Errore = norm(x - xe) / norm(as.matrix(xe))

format(Errore, scientific = TRUE)

Time  = end_time - start_time

Errore
Memory
Time

