library(Matrix)
library(e1071)


A = readMM("../Matrici/ex15.mtx")

xe = rep(1, times = nrow(A))

b = A%*% xe

start_time <- Sys.time()
C = chol(A)
end_time <- Sys.time()

Memory = object.size(chol(A))

y = solve(t(C), b)

x = solve(C, y)


Time  = end_time - start_time

xe = as.matrix(xe)

errore = norm(x - xe) / norm(as.matrix(xe))
format(errore, scientific = TRUE)

Memory
Time