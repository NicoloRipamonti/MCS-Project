library(Matrix)
library(e1071)

start_time <- Sys.time()

A = readMM("../Matrici/ex15.mtx")

xe = rep(1, times = nrow(A))

b = A %*% xe

C = chol(A)

y = solve(t(C), b)

x = solve(C, y)

end_time <- Sys.time()

end_time - start_time

xe = as.matrix(xe)

errore = norm(x - xe) / norm(as.matrix(xe))
format(errore, scientific = TRUE)
